<script setup>
import { ref } from 'vue';
import PlayerCard from '~/components/pages/PlayerCard.vue';
import AddButtton from '../components/AddButtton.vue';

const member = ref({
    player1: {
        id: 1,
        position: 'GK',
        number: 1,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player2: {
        id: 2,
        position: 'GK',
        number: 2,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player3: {
        id: 3,
        position: 'DF',
        number: 3,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player4: {
        id: 4,
        position: 'DF',
        number: 4,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player5: {
        id: 5,
        position: 'DF',
        number: 5,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player6: {
        id: 6,
        position: 'MF',
        number: 6,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player7: {
        id: 7,
        position: 'MF',
        number: 7,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player8: {
        id: 8,
        position: 'MF',
        number: 8,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player9: {
        id: 9,
        position: 'MF',
        number: 9,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player10: {
        id: 10,
        position: 'MF',
        number: 10,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player11: {
        id: 11,
        position: 'FW',
        number: 11,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player12: {
        id: 12,
        position: 'FW',
        number: 12,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player13: {
        id: 13,
        position: 'FW',
        number: 13,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player14: {
        id: 14,
        position: 'FW',
        number: 14,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player15: {
        id: 15,
        position: 'FW',
        number: 15,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player16: {
        id: 16,
        position: 'FW',
        number: 16,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player17: {
        id: 17,
        position: 'FW',
        number: 17,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player18: {
        id: 18,
        position: 'FW',
        number: 18,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player19: {
        id: 19,
        position: 'FW',
        number: 19,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
    player20: {
        id: 20,
        position: 'FW',
        number: 20,
        namae: '長尾 考梓',
        name: 'Tadashi Nagao',
    },
});
</script>

<template>
    <div>
        <v-row>
            <v-col cols="6">
                <h1>メンバー一覧</h1>
            </v-col>
            <v-col cols="6" class="d-flex justify-end">
                <AddButtton />
            </v-col>
        </v-row>
        <v-row>
            <v-col v-for="(player, i) in member" :key="i" cols="12" md="4">
                <PlayerCard :player="player" />
            </v-col>
        </v-row>
    </div>
</template>
