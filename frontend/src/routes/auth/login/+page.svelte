<script>
    import { goto } from '$app/navigation';
    import { Lock, Mail } from 'lucide-svelte';

    let email = $state('');
    let password = $state('');
    let isLoading = $state(false);

    async function handleSubmit(e) {
        e.preventDefault();
        isLoading = true;
        
        // Mock login delay
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        console.log('Login attempt:', { email, password });
        isLoading = false;
        goto('/dashboard');
    }
</script>

<div>
	<h2 class="mt-2 text-center text-2xl font-bold leading-9 tracking-tight text-white">
		Iniciar Sesión
	</h2>
</div>

<div class="mt-10">
	<form class="space-y-6" onsubmit={handleSubmit}>
		<div>
			<label for="email" class="block text-sm font-medium leading-6 text-white">
				Correo Electrónico
			</label>
			<div class="mt-2 relative">
				<div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
					<Mail class="h-5 w-5 text-slate-400" />
				</div>
				<input
					id="email"
					name="email"
					type="email"
					autocomplete="email"
					required
					bind:value={email}
					class="block w-full rounded-md border-0 py-1.5 pl-10 text-slate-900 shadow-sm ring-1 ring-inset ring-slate-300 placeholder:text-slate-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
					placeholder="tu@email.com"
				/>
			</div>
		</div>

		<div>
			<div class="flex items-center justify-between">
				<label for="password" class="block text-sm font-medium leading-6 text-white">
					Contraseña
				</label>
				<div class="text-sm">
					<a href="#" class="font-semibold text-indigo-400 hover:text-indigo-300">
						¿Olvidaste tu contraseña?
					</a>
				</div>
			</div>
			<div class="mt-2 relative">
				<div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
					<Lock class="h-5 w-5 text-slate-400" />
				</div>
				<input
					id="password"
					name="password"
					type="password"
					autocomplete="current-password"
					required
					bind:value={password}
					class="block w-full rounded-md border-0 py-1.5 pl-10 text-slate-900 shadow-sm ring-1 ring-inset ring-slate-300 placeholder:text-slate-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
					placeholder="••••••••"
				/>
			</div>
		</div>

		<div>
			<button
				type="submit"
				disabled={isLoading}
				class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
			>
				{#if isLoading}
					Cargando...
				{:else}
					Iniciar Sesión
				{/if}
			</button>
		</div>
	</form>

	<p class="mt-10 text-center text-sm text-slate-400">
		¿No tienes una cuenta?
		<a href="/auth/signup" class="font-semibold leading-6 text-indigo-400 hover:text-indigo-300">
			Regístrate aquí
		</a>
	</p>
</div>
