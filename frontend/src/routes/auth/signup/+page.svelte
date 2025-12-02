<script>
    import { goto } from '$app/navigation';
    import { Lock, Mail, User } from 'lucide-svelte';

    let name = $state('');
    let email = $state('');
    let password = $state('');
    let confirmPassword = $state('');
    let isLoading = $state(false);

    async function handleSubmit(e) {
        e.preventDefault();
        
        if (password !== confirmPassword) {
            alert('Las contraseñas no coinciden');
            return;
        }

        isLoading = true;
        
        // Mock signup delay
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        console.log('Signup attempt:', { name, email, password });
        isLoading = false;
        goto('/dashboard');
    }
</script>

<div>
	<h2 class="mt-2 text-center text-2xl font-bold leading-9 tracking-tight text-white">
		Crear una cuenta
	</h2>
</div>

<div class="mt-10">
	<form class="space-y-6" onsubmit={handleSubmit}>
		<div>
			<label for="name" class="block text-sm font-medium leading-6 text-white">
				Nombre Completo
			</label>
			<div class="mt-2 relative">
				<div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
					<User class="h-5 w-5 text-slate-400" />
				</div>
				<input
					id="name"
					name="name"
					type="text"
					autocomplete="name"
					required
					bind:value={name}
					class="block w-full rounded-md border-0 py-1.5 pl-10 text-slate-900 shadow-sm ring-1 ring-inset ring-slate-300 placeholder:text-slate-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
					placeholder="Juan Pérez"
				/>
			</div>
		</div>

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
			<label for="password" class="block text-sm font-medium leading-6 text-white">
				Contraseña
			</label>
			<div class="mt-2 relative">
				<div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
					<Lock class="h-5 w-5 text-slate-400" />
				</div>
				<input
					id="password"
					name="password"
					type="password"
					autocomplete="new-password"
					required
					bind:value={password}
					class="block w-full rounded-md border-0 py-1.5 pl-10 text-slate-900 shadow-sm ring-1 ring-inset ring-slate-300 placeholder:text-slate-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
					placeholder="••••••••"
				/>
			</div>
		</div>

		<div>
			<label for="confirm-password" class="block text-sm font-medium leading-6 text-white">
				Confirmar Contraseña
			</label>
			<div class="mt-2 relative">
				<div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
					<Lock class="h-5 w-5 text-slate-400" />
				</div>
				<input
					id="confirm-password"
					name="confirm-password"
					type="password"
					autocomplete="new-password"
					required
					bind:value={confirmPassword}
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
					Registrarse
				{/if}
			</button>
		</div>
	</form>

	<p class="mt-10 text-center text-sm text-slate-400">
		¿Ya tienes una cuenta?
		<a href="/auth/login" class="font-semibold leading-6 text-indigo-400 hover:text-indigo-300">
			Inicia sesión aquí
		</a>
	</p>
</div>
