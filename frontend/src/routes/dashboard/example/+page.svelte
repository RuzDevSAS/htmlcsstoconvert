<script>
	import { Loader2, Image as ImageIcon, Code, FileCode } from 'lucide-svelte';

	let html = $state('<h1>Hello World</h1>\n<p>This is a test.</p>');
	let css = $state('body { background-color: #f0f0f0; font-family: sans-serif; padding: 20px; }\nh1 { color: #333; }');
	let width = $state(800);
	let height = $state(600);
	let loading = $state(false);
	let imageUrl = $state(null);
	let error = $state(null);

	async function generateImage() {
		loading = true;
		error = null;
		imageUrl = null;

		const formData = new FormData();
		formData.append('html', html);
		formData.append('css', css);
		formData.append('width', width.toString());
		formData.append('height', height.toString());

		try {
			const response = await fetch('http://localhost:8000/convert', {
				method: 'POST',
				body: formData
			});

			if (!response.ok) {
				const errorData = await response.json();
				throw new Error(errorData.detail || 'Failed to generate image');
			}

			const contentType = response.headers.get('content-type');
			if (!contentType || !contentType.includes('image')) {
				const text = await response.text();
				throw new Error(`Invalid response type: ${contentType}. Body: ${text.slice(0, 100)}`);
			}

			const blob = await response.blob();
			// Enforce PNG type to ensure browser recognizes it
			const pngBlob = new Blob([blob], { type: 'image/png' });
			imageUrl = URL.createObjectURL(pngBlob);
		} catch (err) {
			console.error(err);
			error = err.message;
		} finally {
			loading = false;
		}
	}
</script>

<div class="p-6 max-w-7xl mx-auto">
	<div class="mb-8">
		<h1 class="text-2xl font-bold text-slate-900 dark:text-white">Test Conversion Endpoint</h1>
		<p class="text-slate-600 dark:text-slate-400">
			Enter HTML and CSS below to generate an image using the backend API.
		</p>
	</div>

	<div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
		<!-- Input Section -->
		<div class="space-y-6">
			<!-- HTML Input -->
			<div class="space-y-2">
				<label
					for="html"
					class="block text-sm font-medium text-slate-700 dark:text-slate-300 flex items-center gap-2"
				>
					<Code class="w-4 h-4" /> HTML
				</label>
				<textarea
					id="html"
					bind:value={html}
					rows="8"
					class="block w-full rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-slate-300 placeholder:text-slate-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 dark:bg-slate-800 dark:text-white dark:ring-slate-700 dark:focus:ring-indigo-500 sm:text-sm sm:leading-6 font-mono"
					placeholder="Enter HTML here..."
				></textarea>
			</div>

			<!-- CSS Input -->
			<div class="space-y-2">
				<label
					for="css"
					class="block text-sm font-medium text-slate-700 dark:text-slate-300 flex items-center gap-2"
				>
					<FileCode class="w-4 h-4" /> CSS
				</label>
				<textarea
					id="css"
					bind:value={css}
					rows="8"
					class="block w-full rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-slate-300 placeholder:text-slate-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 dark:bg-slate-800 dark:text-white dark:ring-slate-700 dark:focus:ring-indigo-500 sm:text-sm sm:leading-6 font-mono"
					placeholder="Enter CSS here..."
				></textarea>
			</div>

			<!-- Dimensions -->
			<div class="grid grid-cols-2 gap-4">
				<div class="space-y-2">
					<label for="width" class="block text-sm font-medium text-slate-700 dark:text-slate-300"
						>Width</label
					>
					<input
						type="number"
						id="width"
						bind:value={width}
						class="block w-full rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-slate-300 placeholder:text-slate-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 dark:bg-slate-800 dark:text-white dark:ring-slate-700 dark:focus:ring-indigo-500 sm:text-sm sm:leading-6"
					/>
				</div>
				<div class="space-y-2">
					<label for="height" class="block text-sm font-medium text-slate-700 dark:text-slate-300"
						>Height</label
					>
					<input
						type="number"
						id="height"
						bind:value={height}
						class="block w-full rounded-md border-0 py-1.5 text-slate-900 shadow-sm ring-1 ring-inset ring-slate-300 placeholder:text-slate-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 dark:bg-slate-800 dark:text-white dark:ring-slate-700 dark:focus:ring-indigo-500 sm:text-sm sm:leading-6"
					/>
				</div>
			</div>

			<button
				onclick={generateImage}
				disabled={loading}
				class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 disabled:opacity-50 disabled:cursor-not-allowed items-center gap-2"
			>
				{#if loading}
					<Loader2 class="w-4 h-4 animate-spin" />
					Generating...
				{:else}
					Generate Image
				{/if}
			</button>

			{#if error}
				<div class="rounded-md bg-red-50 p-4 dark:bg-red-900/20">
					<div class="flex">
						<div class="ml-3">
							<h3 class="text-sm font-medium text-red-800 dark:text-red-400">Error</h3>
							<div class="mt-2 text-sm text-red-700 dark:text-red-300">
								<p>{error}</p>
							</div>
						</div>
					</div>
				</div>
			{/if}
		</div>

		<!-- Output Section -->
		<div
			class="bg-slate-100 dark:bg-slate-900 rounded-lg border border-slate-200 dark:border-slate-700 flex items-center justify-center min-h-[400px] overflow-hidden relative bg-[url('https://res.cloudinary.com/practicaldev/image/fetch/s--_MCEk7P6--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/1wwdyw5de8avrdkgtz5n.png')] bg-repeat"
		>
			{#if imageUrl}
				<img
					src={imageUrl}
					alt="Generated"
					class="max-w-full max-h-full object-contain shadow-lg bg-white/0"
				/>
				<a
					href={imageUrl}
					download="generated.png"
					class="absolute bottom-4 right-4 bg-white dark:bg-slate-800 text-slate-900 dark:text-white px-3 py-2 rounded-md shadow-sm text-sm font-medium hover:bg-slate-50 dark:hover:bg-slate-700 border border-slate-200 dark:border-slate-600 z-10"
				>
					Download
				</a>
			{:else}
				<div
					class="text-center text-slate-400 dark:text-slate-500 bg-white/80 dark:bg-slate-900/80 p-4 rounded-lg backdrop-blur-sm"
				>
					<ImageIcon class="w-12 h-12 mx-auto mb-2 opacity-50" />
					<p>Generated image will appear here</p>
				</div>
			{/if}
		</div>
	</div>

	<!-- Code Display Section -->
	<div class="mt-12 grid grid-cols-1 lg:grid-cols-2 gap-8">
		<div class="space-y-4">
			<h2 class="text-xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
				<Code class="w-5 h-5" /> HTML Code
			</h2>
			<div class="relative group">
				<pre
					class="bg-slate-900 text-slate-50 p-4 rounded-lg overflow-x-auto font-mono text-sm border border-slate-700"><code
						>{html}</code
					></pre>
			</div>
		</div>

		<div class="space-y-4">
			<h2 class="text-xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
				<FileCode class="w-5 h-5" /> CSS Code
			</h2>
			<div class="relative group">
				<pre
					class="bg-slate-900 text-slate-50 p-4 rounded-lg overflow-x-auto font-mono text-sm border border-slate-700"><code
						>{css}</code
					></pre>
			</div>
		</div>
	</div>

	<!-- API Usage Example -->
	<div class="mt-12 space-y-6">
		<h2
			class="text-2xl font-bold text-slate-900 dark:text-white border-b border-slate-200 dark:border-slate-800 pb-4"
		>
			API Usage Example
		</h2>

		<div class="space-y-4">
			<h3 class="text-lg font-semibold text-slate-800 dark:text-slate-200">cURL</h3>
			<pre
				class="bg-slate-900 text-slate-50 p-4 rounded-lg overflow-x-auto font-mono text-sm border border-slate-700"><code
					>curl -X POST http://localhost:8000/convert \
  -F "html=&lt;h1&gt;Hello World&lt;/h1&gt;" \
  -F "css=h1 &#123; color: red; &#125;" \
  -F "width=800" \
  -F "height=600" \
  --output image.png</code
				></pre>
		</div>

		<div class="space-y-4">
			<h3 class="text-lg font-semibold text-slate-800 dark:text-slate-200">JavaScript (Fetch)</h3>
			<pre
				class="bg-slate-900 text-slate-50 p-4 rounded-lg overflow-x-auto font-mono text-sm border border-slate-700"><code
					>const formData = new FormData();
formData.append('html', '&lt;h1&gt;Hello World&lt;/h1&gt;');
formData.append('css', 'h1 &#123; color: red; &#125;');
formData.append('width', '800');
formData.append('height', '600');

const response = await fetch('http://localhost:8000/convert', &#123;
  method: 'POST',
  body: formData
&#125;);

const blob = await response.blob();
// Use the blob (e.g., download or display)</code
				></pre>
		</div>
	</div>
</div>
