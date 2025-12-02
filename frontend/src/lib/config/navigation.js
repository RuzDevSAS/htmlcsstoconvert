import { Home, Image, Settings, FileText } from 'lucide-svelte';

export const navigation = [
    {
        label: 'Dashboard',
        href: '/dashboard',
        icon: Home
    },
    {
        label: 'Convert',
        href: '/dashboard/example',
        icon: Image
    },
    {
        label: 'Documentation',
        href: '/docs',
        icon: FileText
    },
    {
        label: 'Settings',
        href: '/settings',
        icon: Settings
    }
];
