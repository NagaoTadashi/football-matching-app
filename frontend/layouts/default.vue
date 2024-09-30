<script setup>
import { ref, watch } from 'vue';
import { getAuth, signOut } from 'firebase/auth';

const items = [
    {
        icon: 'mdi-soccer-field',
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
        icon: 'mdi-text-box-outline',
        title: '対戦相手を募集する',
        value: 'requirementOpponent',
        to: '/RequirementOpponent',
    },
    {
        icon: 'mdi-account-search',
        title: '対戦相手を探す',
        value: 'findOpponent',
        to: '/FindOpponent',
    },
];

const group = ref(null);
const drawer = ref(null);

watch(group, () => {
    drawer.value = false;
});

const handleSignOut = async () => {
    const auth = getAuth();
    try {
        await signOut(auth);
        console.log('Sign-out successful.');
    } catch (error) {
        console.error('An error happened during sign-out:', error);
    }
};
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
            <v-app-bar-title>
                <v-icon>mdi-soccer</v-icon> Football Match</v-app-bar-title
            >
            <v-spacer></v-spacer>

            <v-btn
                class="text-none"
                stacked
                v-tooltip:bottom="'他チームからの申し込み'"
            >
                <v-badge color="error" content="2">
                    <v-icon>mdi-email-outline</v-icon>
                </v-badge>
            </v-btn>

            <v-btn class="text-none" stacked v-tooltip:bottom="'通知'">
                <v-badge color="error" content="2">
                    <v-icon>mdi-bell-outline</v-icon>
                </v-badge>
            </v-btn>

            <v-btn
                class="text-none"
                stacked
                v-tooltip:bottom="'ログアウト'"
                @click="handleSignOut"
            >
                <v-icon>mdi-logout</v-icon>
            </v-btn>
        </v-app-bar>

        <v-navigation-drawer floating permanent width="225">
            <v-list density="compact" nav>
                <v-list-item
                    v-for="(item, index) in items"
                    :key="index"
                    :link="true"
                    :to="item.to"
                    :prepend-icon="item.icon"
                    :title="item.title"
                ></v-list-item>
            </v-list>
        </v-navigation-drawer>

        <v-main>
            <v-container>
                <slot />
            </v-container>
        </v-main>
    </v-app>
</template>
