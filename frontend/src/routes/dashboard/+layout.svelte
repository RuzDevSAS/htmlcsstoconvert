<script>
	import Sidebar from '$lib/components/Sidebar.svelte';
	let { children } = $props();
	let isCollapsed = $state(false);
</script>

<div class="min-h-screen bg-white dark:bg-slate-950">
	<Sidebar bind:isCollapsed />
	<main class="transition-all duration-300 {isCollapsed ? 'pl-16' : 'pl-64'}">
		{@render children()}
	</main>
</div>
