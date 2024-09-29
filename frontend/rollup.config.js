// frontend/rollup.config.js
import svelte from 'rollup-plugin-svelte';
import commonjs from '@rollup/plugin-commonjs';
import terser from '@rollup/plugin-terser';
import resolve from '@rollup/plugin-node-resolve';
import livereload from 'rollup-plugin-livereload';
import css from 'rollup-plugin-css-only';
import serve from 'rollup-plugin-serve';

const production = !process.env.ROLLUP_WATCH;

export default {
    input: 'src/main.js',
    output: {
        sourcemap: true,
        format: 'iife',
        name: 'app',
        file: 'public/build/bundle.js'
    },
    plugins: [
        svelte({
            compilerOptions: {
                dev: !production
            }
        }),
        // Extract component CSS into a separate file
        css({ output: 'bundle.css' }),

        // Resolve node modules
        resolve({
            browser: true,
            dedupe: ['svelte'],
            exportConditions: ['svelte']
        }),
        commonjs(),

        // In development, serve the app and enable HMR with history API fallback
        !production && serve({
            open: true,
            contentBase: 'public',
            historyApiFallback: true, // Handles client-side routing
            port: 5000,               // Ensure this matches FRONTEND_PORT
            host: '0.0.0.0'           // Bind to all interfaces for Docker
        }),

        // Watch the `public` directory and refresh the browser on changes when not in production
        !production && livereload({
            watch: 'public',
            port: 35729,
            hostname: '0.0.0.0'  // Ensures LiveReload is accessible from the host
        }),

        // If we're building for production, minify
        production && terser()
    ],
    watch: {
        clearScreen: false,
        chokidar: {
            usePolling: true,       // Enable polling
            interval: 1000,         // Poll every second
            binaryInterval: 3000,   // Poll binary files every 3 seconds
            followSymlinks: false,
            ignored: /node_modules/
        }
    }
};
