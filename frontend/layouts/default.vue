<script setup>
import { ref } from 'vue';
import NavigationDrawer from '~/components/NavigationDrawer.vue';

const drawer = ref(null);
</script>

<template>
    <v-app id="inspire">
        <v-system-bar>
            <v-spacer></v-spacer>

            <v-icon>mdi-square</v-icon>

            <v-icon>mdi-circle</v-icon>

            <v-icon>mdi-triangle</v-icon>
        </v-system-bar>

        <v-app-bar>
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

            <v-app-bar-title>Application</v-app-bar-title>
        </v-app-bar>

        <NavigationDrawer v-model="drawer" />

        <v-main class="bg-grey-lighten-2">
            <v-container>
                <slot />
            </v-container>
        </v-main>
    </v-app>
</template>
