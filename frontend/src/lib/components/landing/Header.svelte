<script>
    import { Github, Menu, X } from 'lucide-svelte';
    import { page } from '$app/stores';

    let isMenuOpen = $state(false);

    function toggleMenu() {
        isMenuOpen = !isMenuOpen;
    }
</script>

<header
	class="fixed top-0 left-0 right-0 z-50 border-b border-white/10 bg-slate-950/80 backdrop-blur-md"
>
	<nav class="mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8" aria-label="Global">
		<div class="flex lg:flex-1">
			<a href="/" class="-m-1.5 p-1.5 text-xl font-bold text-white">
				HTML <span class="text-indigo-400">Convert</span>
			</a>
		</div>
		<div class="flex lg:hidden">
			<button
				type="button"
				class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-slate-300 hover:text-white"
				onclick={toggleMenu}
			>
				<span class="sr-only">Open main menu</span>
				{#if isMenuOpen}
					<X class="h-6 w-6" aria-hidden="true" />
				{:else}
					<Menu class="h-6 w-6" aria-hidden="true" />
				{/if}
			</button>
		</div>
		<div class="hidden lg:flex lg:gap-x-12">
			<a
				href="#features"
				class="text-sm font-semibold leading-6 text-slate-300 hover:text-white transition-colors"
				>Features</a
			>
			<a
				href="#pricing"
				class="text-sm font-semibold leading-6 text-slate-300 hover:text-white transition-colors"
				>Pricing</a
			>
			<a
				href="https://github.com/RuzDevSAS/htmlcsstoconvert"
				target="_blank"
				class="text-sm font-semibold leading-6 text-slate-300 hover:text-white transition-colors flex items-center gap-2"
			>
				GitHub
			</a>
		</div>
		<div class="hidden lg:flex lg:flex-1 lg:justify-end">
			<a
				href="/auth/login"
				class="text-sm font-semibold leading-6 text-white bg-indigo-600 hover:bg-indigo-500 px-4 py-2 rounded-lg transition-colors"
			>
				Iniciar Sesión <span aria-hidden="true">&rarr;</span>
			</a>
		</div>
	</nav>
	<!-- Mobile menu, show/hide based on menu state. -->
	{#if isMenuOpen}
		<div class="lg:hidden" role="dialog" aria-modal="true">
			<!-- Background backdrop, show/hide based on slide-over state. -->
			<div class="fixed inset-0 z-50"></div>
			<div
				class="fixed inset-y-0 right-0 z-50 w-full overflow-y-auto bg-slate-900 px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-white/10"
			>
				<div class="flex items-center justify-between">
					<a href="/" class="-m-1.5 p-1.5 text-xl font-bold text-white">
						HTML <span class="text-indigo-400">Convert</span>
					</a>
					<button
						type="button"
						class="-m-2.5 rounded-md p-2.5 text-slate-300 hover:text-white"
						onclick={toggleMenu}
					>
						<span class="sr-only">Close menu</span>
						<X class="h-6 w-6" aria-hidden="true" />
					</button>
				</div>
				<div class="mt-6 flow-root">
					<div class="-my-6 divide-y divide-gray-500/10">
						<div class="space-y-2 py-6">
							<a
								href="#features"
								class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-white hover:bg-slate-800"
								onclick={toggleMenu}>Features</a
							>
							<a
								href="#pricing"
								class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-white hover:bg-slate-800"
								onclick={toggleMenu}>Pricing</a
							>
							<a
								href="https://github.com/RuzDevSAS/htmlcsstoconvert"
								target="_blank"
								class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-white hover:bg-slate-800"
								onclick={toggleMenu}>GitHub</a
							>
						</div>
						<div class="py-6">
							<a
								href="/auth/login"
								class="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-white hover:bg-slate-800"
								onclick={toggleMenu}>Iniciar Sesión</a
							>
						</div>
					</div>
				</div>
			</div>
		</div>
	{/if}
</header>
