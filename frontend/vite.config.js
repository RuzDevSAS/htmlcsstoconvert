import tailwindcss from '@tailwindcss/vite';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [tailwindcss(), sveltekit()],
	server: {
		allowedHosts: [
			'htmlcssconvert-app-v04xrn-176dda-212-56-40-86.traefik.me',
			'htmlcssconvert.ruzdev.online'
		]
	}
});
