<script>
	import { 
		Code, 
		Cloud, 
		Check, 
		Github, 
		Terminal, 
		Zap, 
		Server, 
		Shield 
	} from 'lucide-svelte';
</script>

<div
	class="min-h-screen bg-slate-950 text-white font-sans selection:bg-indigo-500 selection:text-white"
>
	<!-- Hero Section -->
	<header class="relative overflow-hidden pt-24 pb-16 lg:pb-32 lg:pt-40">
		<div class="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80">
			<div
				class="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-20 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]"
			></div>
		</div>

		<div class="mx-auto max-w-7xl px-6 lg:px-8">
			<div class="mx-auto max-w-2xl text-center">
				<h1 class="text-4xl font-bold tracking-tight text-white sm:text-6xl">
					Convert HTML/CSS to <span class="text-indigo-400">Any Format</span>
				</h1>
				<p class="mt-6 text-lg leading-8 text-slate-300">
					The ultimate open-source solution for rendering HTML & CSS. Self-host for complete control
					or use our managed cloud API for instant scalability.
				</p>
				<div class="mt-10 flex items-center justify-center gap-x-6">
					<a
						href="#pricing"
						class="rounded-md bg-indigo-500 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
					>
						Get Started
					</a>
					<a
						href="https://github.com/RuzDevSAS/htmlcsstoconvert"
						target="_blank"
						class="text-sm font-semibold leading-6 text-white flex items-center gap-2 hover:text-indigo-300 transition-colors"
					>
						<Github class="h-5 w-5" />
						View on GitHub <span aria-hidden="true">→</span>
					</a>
				</div>
			</div>
		</div>
	</header>

	<!-- Features Section -->
	<section class="py-24 sm:py-32 bg-slate-900/50">
		<div class="mx-auto max-w-7xl px-6 lg:px-8">
			<div class="mx-auto max-w-2xl lg:text-center">
				<h2 class="text-base font-semibold leading-7 text-indigo-400">Deploy Your Way</h2>
				<p class="mt-2 text-3xl font-bold tracking-tight text-white sm:text-4xl">
					Open Source Power, Cloud Convenience
				</p>
				<p class="mt-6 text-lg leading-8 text-slate-300">
					Choose the deployment model that fits your needs. Whether you need data privacy with
					self-hosting or ease of use with our cloud API.
				</p>
			</div>
			<div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-4xl">
				<dl
					class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-10 lg:max-w-none lg:grid-cols-2 lg:gap-y-16"
				>
					<div class="relative pl-16">
						<dt class="text-base font-semibold leading-7 text-white">
							<div
								class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-500/10 ring-1 ring-indigo-500/20"
							>
								<Terminal class="h-6 w-6 text-indigo-400" />
							</div>
							Open Source Core
						</dt>
						<dd class="mt-2 text-base leading-7 text-slate-300">
							Full access to the source code. Run it on your own infrastructure, customize it to
							your needs, and contribute back to the community.
						</dd>
					</div>
					<div class="relative pl-16">
						<dt class="text-base font-semibold leading-7 text-white">
							<div
								class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-500/10 ring-1 ring-indigo-500/20"
							>
								<Cloud class="h-6 w-6 text-indigo-400" />
							</div>
							Managed Cloud API
						</dt>
						<dd class="mt-2 text-base leading-7 text-slate-300">
							Skip the DevOps. Use our high-performance, scalable API to convert HTML/CSS to images,
							PDFs, and more instantly.
						</dd>
					</div>
					<div class="relative pl-16">
						<dt class="text-base font-semibold leading-7 text-white">
							<div
								class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-500/10 ring-1 ring-indigo-500/20"
							>
								<Zap class="h-6 w-6 text-indigo-400" />
							</div>
							Lightning Fast
						</dt>
						<dd class="mt-2 text-base leading-7 text-slate-300">
							Optimized rendering engine ensures your conversions happen in milliseconds, not
							seconds.
						</dd>
					</div>
					<div class="relative pl-16">
						<dt class="text-base font-semibold leading-7 text-white">
							<div
								class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-500/10 ring-1 ring-indigo-500/20"
							>
								<Shield class="h-6 w-6 text-indigo-400" />
							</div>
							Secure & Private
						</dt>
						<dd class="mt-2 text-base leading-7 text-slate-300">
							Enterprise-grade security. Your data is processed securely and never stored longer
							than necessary.
						</dd>
					</div>
				</dl>
			</div>
		</div>
	</section>

	<!-- Pricing Section -->
	<section id="pricing" class="py-24 sm:py-32">
		<div class="mx-auto max-w-7xl px-6 lg:px-8">
			<div class="mx-auto max-w-2xl sm:text-center">
				<h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">
					Simple, Transparent Pricing
				</h2>
				<p class="mt-6 text-lg leading-8 text-slate-300">
					Start for free with our open-source version or upgrade to our cloud platform for managed
					services.
				</p>
			</div>
			<div
				class="mx-auto mt-16 grid max-w-lg grid-cols-1 items-center gap-y-6 sm:mt-20 sm:gap-y-0 lg:max-w-4xl lg:grid-cols-2"
			>
				<!-- Open Source Plan -->
				<div
					class="rounded-3xl p-8 ring-1 ring-white/10 sm:p-10 bg-slate-900/50 sm:rounded-r-none lg:rounded-r-none lg:rounded-bl-3xl"
				>
					<h3 class="text-base font-semibold leading-7 text-indigo-400">Open Source</h3>
					<p class="mt-4 flex items-baseline gap-x-2">
						<span class="text-5xl font-bold tracking-tight text-white">$0</span>
						<span class="text-base text-slate-400">/forever</span>
					</p>
					<p class="mt-6 text-base leading-7 text-slate-300">
						Perfect for hobbyists and developers who want full control.
					</p>
					<ul role="list" class="mt-8 space-y-3 text-sm leading-6 text-slate-300">
						<li class="flex gap-x-3">
							<Check class="h-6 w-5 flex-none text-indigo-400" /> Self-hosted
						</li>
						<li class="flex gap-x-3">
							<Check class="h-6 w-5 flex-none text-indigo-400" /> Community Support
						</li>
						<li class="flex gap-x-3">
							<Check class="h-6 w-5 flex-none text-indigo-400" /> Unlimited Conversions (Your Hardware)
						</li>
						<li class="flex gap-x-3">
							<Check class="h-6 w-5 flex-none text-indigo-400" /> MIT License
						</li>
					</ul>
					<a
						href="https://github.com"
						class="mt-8 block rounded-md px-3 py-2 text-center text-sm font-semibold leading-6 text-indigo-400 ring-1 ring-inset ring-indigo-400/20 hover:ring-indigo-400/30 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
					>
						View Source Code
					</a>
				</div>

				<!-- Cloud Plan -->
				<div
					class="relative rounded-3xl p-8 ring-1 ring-white/10 sm:p-10 bg-slate-800 shadow-2xl sm:rounded-l-none lg:rounded-l-none lg:rounded-tr-3xl"
				>
					<div
						class="absolute top-0 right-0 -mt-4 mr-4 rounded-full bg-indigo-500 px-3 py-1 text-xs font-semibold text-white shadow-sm"
					>
						Most Popular
					</div>
					<h3 class="text-base font-semibold leading-7 text-indigo-400">Pro Cloud</h3>
					<p class="mt-4 flex items-baseline gap-x-2">
						<span class="text-5xl font-bold tracking-tight text-white">$29</span>
						<span class="text-base text-slate-400">/month</span>
					</p>
					<p class="mt-6 text-base leading-7 text-slate-300">
						For businesses that need reliability and scale without the hassle.
					</p>
					<ul role="list" class="mt-8 space-y-3 text-sm leading-6 text-slate-300">
						<li class="flex gap-x-3">
							<Check class="h-6 w-5 flex-none text-indigo-400" /> Managed API Access
						</li>
						<li class="flex gap-x-3">
							<Check class="h-6 w-5 flex-none text-indigo-400" /> Priority Email Support
						</li>
						<li class="flex gap-x-3">
							<Check class="h-6 w-5 flex-none text-indigo-400" /> 10,000 Conversions / mo
						</li>
						<li class="flex gap-x-3">
							<Check class="h-6 w-5 flex-none text-indigo-400" /> 99.9% Uptime SLA
						</li>
						<li class="flex gap-x-3">
							<Check class="h-6 w-5 flex-none text-indigo-400" /> No Server Management
						</li>
					</ul>
					<a
						href="#"
						class="mt-8 block rounded-md bg-indigo-500 px-3 py-2 text-center text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
					>
						Start Free Trial
					</a>
				</div>
			</div>
		</div>
	</section>

	<!-- Footer -->
	<footer class="bg-slate-900 border-t border-white/10">
		<div class="mx-auto max-w-7xl overflow-hidden px-6 py-20 sm:py-24 lg:px-8">
			<nav class="-mb-6 columns-2 sm:flex sm:justify-center sm:space-x-12" aria-label="Footer">
				<div class="pb-6">
					<a href="#" class="text-sm leading-6 text-slate-400 hover:text-white">About</a>
				</div>
				<div class="pb-6">
					<a href="#" class="text-sm leading-6 text-slate-400 hover:text-white">Blog</a>
				</div>
				<div class="pb-6">
					<a href="#" class="text-sm leading-6 text-slate-400 hover:text-white">Jobs</a>
				</div>
				<div class="pb-6">
					<a href="#" class="text-sm leading-6 text-slate-400 hover:text-white">Press</a>
				</div>
				<div class="pb-6">
					<a href="#" class="text-sm leading-6 text-slate-400 hover:text-white">Accessibility</a>
				</div>
				<div class="pb-6">
					<a href="#" class="text-sm leading-6 text-slate-400 hover:text-white">Partners</a>
				</div>
			</nav>
			<div class="mt-10 flex justify-center space-x-10">
				<a href="https://github.com" class="text-slate-400 hover:text-white">
					<span class="sr-only">GitHub</span>
					<Github class="h-6 w-6" />
				</a>
			</div>
			<p class="mt-10 text-center text-xs leading-5 text-slate-500">
				&copy; 2024 HTML/CSS Converter, Inc. All rights reserved.
			</p>
		</div>
	</footer>
</div>
