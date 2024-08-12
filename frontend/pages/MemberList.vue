<script setup>
import { ref } from 'vue';

const member = {
    player1: {
        id: 1,
        number: 1,
        name: 'player1',
        position: 'GK',
    },
    player2: {
        id: 2,
        number: 2,
        name: 'player2',
        position: 'GK',
    },
    player3: {
        id: 3,
        number: 3,
        name: 'player3',
        position: 'DF',
    },
    player4: {
        id: 4,
        number: 4,
        name: 'player4',
        position: 'DF',
    },
    player5: {
        id: 5,
        number: 5,
        name: 'player5',
        position: 'DF',
    },
    player6: {
        id: 6,
        number: 6,
        name: 'player6',
        position: 'MF',
    },
    player7: {
        id: 7,
        number: 7,
        name: 'player7',
        position: 'MF',
    },
    player8: {
        id: 8,
        number: 8,
        name: 'player8',
        position: 'MF',
    },
    player9: {
        id: 9,
        number: 9,
        name: 'player9',
        position: 'MF',
    },
    player10: {
        id: 10,
        number: 10,
        name: 'player10',
        position: 'MF',
    },
    player11: {
        id: 11,
        number: 11,
        name: 'player11',
        position: 'FW',
    },
    player12: {
        id: 12,
        number: 12,
        name: 'player12',
        position: 'FW',
    },
    player13: {
        id: 13,
        number: 13,
        name: 'player13',
        position: 'FW',
    },
    player14: {
        id: 14,
        number: 14,
        name: 'player14',
        position: 'FW',
    },
    player15: {
        id: 15,
        number: 15,
        name: 'player15',
        position: 'FW',
    },
    player16: {
        id: 16,
        number: 16,
        name: 'player16',
        position: 'FW',
    },
    player17: {
        id: 17,
        number: 17,
        name: 'player17',
        position: 'FW',
    },
    player18: {
        id: 18,
        number: 18,
        name: 'player18',
        position: 'FW',
    },
    player19: {
        id: 19,
        number: 19,
        name: 'player19',
        position: 'FW',
    },
    player20: {
        id: 20,
        number: 20,
        name: 'player20',
        position: 'FW',
    },
};

const color = ref('primary');
const variant = ref('tonal');
</script>

<template>
    <div>
        <v-row>
            <v-col class="mt-2" cols="12">
                <h1>メンバー一覧</h1>
            </v-col>
            <v-col v-for="(player, i) in member" :key="i" cols="12" md="4">
                <v-card :variant="variant" class="mx-auto" elevation="3">
                    <v-card-item>
                        <v-card-title>No. {{ player.number }} </v-card-title>
                        <v-card-title
                            >{{ player.position }}
                            {{ player.name }}</v-card-title
                        >
                    </v-card-item>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>
