<script setup>
import { ref, watch } from 'vue';

const items = [
    {
        title: '試合日程・結果',
        value: 'match',
    },
    {
        title: 'メンバー',
        value: 'mumber',
    },
    {
        title: '対戦相手を探す',
        value: 'findOpponent',
    },
];

const group = ref(null);

watch(group, () => {
    drawer.value = false;
});
</script>

<template>
    <v-navigation-drawer
        v-model="drawer"
        :location="$vuetify.display.mobile ? 'bottom' : undefined"
        temporary
    >
        <v-list :items="items"></v-list>
    </v-navigation-drawer>
</template>
