<script setup>
import { ref, watch } from 'vue';

const items = [
    {
        icon: 'mdi-calendar-month',
        title: '試合日程・結果',
        value: 'matchList',
        to: '/',
    },
    {
        icon: 'mdi-tshirt-crew',
        title: 'チーム情報',
        value: 'teamInfo',
        to: '/TeamInfo',
    },
    {
        icon: 'mdi-account-group',
        title: '選手一覧',
        value: 'playerList',
        to: '/PlayerList',
    },
    {
        icon: 'mdi-calendar-month',
        title: '試合日程・結果',
        value: 'match',
        to: '/MatchList',
    },
    {
        icon: 'mdi-account-search',
        title: '対戦相手を探す',
        value: 'findOpponent',
        to: '/FindOpponent',
    },
    {
        icon: 'mdi-soccer-field',
        title: '試合を登録',
        value: 'registrationMatch',
        to: '/RegistrationMatch',
    },
];

const group = ref(null);
const drawer = ref(null);

watch(group, () => {
    drawer.value = false;
});
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

            <v-app-bar-title>Football Match</v-app-bar-title>
        </v-app-bar>

        <v-navigation-drawer
            v-model="drawer"
            width="220"
            :location="$vuetify.display.mobile ? 'bottom' : undefined"
            temporary
        >
            <v-list-item
                v-for="(item, index) in items"
                :key="index"
                :link="true"
                :to="item.to"
                :prepend-icon="item.icon"
                :title="item.title"
            ></v-list-item>
        </v-navigation-drawer>

        <v-main
            class="d-flex align-center justify-center"
            style="min-height: 300px"
        >
            <v-container>
                <slot />
            </v-container>
        </v-main>
    </v-app>
</template>
