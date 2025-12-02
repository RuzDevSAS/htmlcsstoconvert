<script>
    import { page } from '$app/stores';
    import { goto } from '$app/navigation';
    import { navigation } from '$lib/config/navigation';
    import { PanelLeft, LogOut } from 'lucide-svelte';

    let { isCollapsed = $bindable(false) } = $props();

    function cerrarSesion() {
        console.log('Cerrar sesión');
        goto('/');
    }
</script>

<aside
	class="fixed inset-y-0 left-0 z-50 bg-white border-r border-slate-200 dark:bg-slate-950 dark:border-slate-800 transition-all duration-300 {isCollapsed
		? 'w-16'
		: 'w-64'}"
>
	<div class="flex flex-col h-full">
		<!-- Logo/Brand -->
		<div
			class="flex items-center justify-between h-16 px-4 border-b border-slate-200 dark:border-slate-800"
		>
			{#if !isCollapsed}
				<span
					class="text-lg font-bold text-slate-900 dark:text-white whitespace-nowrap overflow-hidden"
					>HTML Convert</span
				>
			{/if}
			<button
				onclick={() => (isCollapsed = !isCollapsed)}
				class="p-1.5 rounded-lg text-slate-500 hover:bg-slate-100 dark:text-slate-400 dark:hover:bg-slate-800 transition-colors {isCollapsed
					? 'mx-auto'
					: ''}"
				aria-label="Toggle Sidebar"
			>
				<PanelLeft class="w-5 h-5" />
			</button>
		</div>

		<!-- Navigation -->
		<nav class="flex-1 px-2 py-6 space-y-1">
			{#each navigation as item}
				{@const isActive = $page.url.pathname === item.href}
				<a
					href={item.href}
					class="flex items-center px-2 py-3 text-sm font-medium rounded-lg transition-colors group relative
                    {isActive
						? 'bg-blue-50 text-blue-700 dark:bg-blue-900/20 dark:text-blue-400'
						: 'text-slate-600 hover:bg-slate-50 dark:text-slate-400 dark:hover:bg-slate-900'}
                    {isCollapsed ? 'justify-center' : ''}"
				>
					<item.icon class="w-5 h-5 {isCollapsed ? '' : 'mr-3'} flex-shrink-0" />
					{#if !isCollapsed}
						<span class="whitespace-nowrap overflow-hidden">{item.label}</span>
					{/if}

					{#if isCollapsed}
						<!-- Tooltip for collapsed state -->
						<div
							class="absolute left-full ml-2 px-2 py-1 bg-slate-800 text-white text-xs rounded opacity-0 group-hover:opacity-100 pointer-events-none whitespace-nowrap z-50"
						>
							{item.label}
						</div>
					{/if}
				</a>
			{/each}
		</nav>

		<!-- User/Footer -->
		<div class="p-4 border-t border-slate-200 dark:border-slate-800 flex flex-col gap-4">
			<div class="flex items-center {isCollapsed ? 'justify-center' : ''}">
				<div class="w-8 h-8 rounded-full bg-slate-200 dark:bg-slate-800 flex-shrink-0"></div>
				{#if !isCollapsed}
					<div class="ml-3 overflow-hidden">
						<p class="text-sm font-medium text-slate-900 dark:text-white truncate">User</p>
						<p class="text-xs text-slate-500 dark:text-slate-400 truncate">user@example.com</p>
					</div>
				{/if}
			</div>

			<button
				onclick={cerrarSesion}
				class="flex items-center {isCollapsed
					? 'justify-center'
					: 'px-2'} py-2 text-sm font-medium text-red-600 hover:bg-red-50 dark:text-red-400 dark:hover:bg-red-900/20 rounded-lg transition-colors w-full group relative"
				aria-label="Cerrar Sesión"
			>
				<LogOut class="w-5 h-5 {isCollapsed ? '' : 'mr-3'} flex-shrink-0" />
				{#if !isCollapsed}
					<span class="whitespace-nowrap overflow-hidden">Cerrar Sesión</span>
				{/if}

				{#if isCollapsed}
					<!-- Tooltip for collapsed state -->
					<div
						class="absolute left-full ml-2 px-2 py-1 bg-slate-800 text-white text-xs rounded opacity-0 group-hover:opacity-100 pointer-events-none whitespace-nowrap z-50"
					>
						Cerrar Sesión
					</div>
				{/if}
			</button>
		</div>
	</div>
</aside>
