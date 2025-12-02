<script>
    let { children } = $props();
</script>

<div class="min-h-screen bg-slate-950 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
	<div class="sm:mx-auto sm:w-full sm:max-w-md">
		<a href="/" class="flex justify-center text-3xl font-bold text-white">
			HTML <span class="text-indigo-400 ml-1">Convert</span>
		</a>
	</div>

	<div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
		<div class="bg-slate-900 py-8 px-4 shadow sm:rounded-lg sm:px-10 border border-slate-800">
			{@render children()}
		</div>
	</div>
</div>
