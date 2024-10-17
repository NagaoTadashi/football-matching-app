// https://nuxt.com/docs/api/configuration/nuxt-config
import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify';

export default defineNuxtConfig({
    compatibilityDate: '2024-04-03',
    devtools: { enabled: true },
    ssr: false,
    build: {
        transpile: ['vuetify'],
    },
    modules: [
        (_options, nuxt) => {
            nuxt.hooks.hook('vite:extendConfig', (config) => {
                // @ts-expect-error
                config.plugins.push(vuetify({ autoImport: true }));
            });
        },
        'nuxt-vuefire',
    ],
    vite: {
        vue: {
            template: {
                transformAssetUrls,
            },
        },
    },
    runtimeConfig: {
        public: {
            apiUrl: process.env.NUXT_PUBLIC_API_URL || '',
            apiKey: process.env.NUXT_API_KEY || '',
            authDomain: process.env.NUXT_AUTH_DOMAIN || '',
            projectId: process.env.NUXT_PROJECT_ID || '',
            storageBucket: process.env.NUXT_STORAGE_BUCKET || '',
            messagingSenderId: process.env.NUXT_MESSAGING_SENDER_ID || '',
            appId: process.env.NUXT_APP_ID || '',
            measurementId: process.env.NUXT_MEASUREMENT_ID || '',
        },
    },
    vuefire: {
        auth: {
            enabled: true,
        },
        config: {
            apiKey: process.env.NUXT_PUBLIC_API_KEY,
            authDomain: process.env.NUXT_PUBLIC_AUTH_DOMAIN,
            projectId: process.env.NUXT_PUBLIC_PROJECT_ID,
            storageBucket: process.env.NUXT_PUBLIC_STORAGE_BUCKET,
            messagingSenderId: process.env.NUXT_PUBLIC_MESSAGING_SENDER_ID,
            appId: process.env.NUXT_PUBLIC_APP_ID,
            measurementId: process.env.NUXT_PUBLIC_MEASUREMENT_ID,
        },
    },
});
