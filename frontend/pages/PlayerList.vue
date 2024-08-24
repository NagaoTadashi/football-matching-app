<script setup>
import AddButtton from '../components/pages/playerlist/AddButtton.vue';
import PlayerCard from '~/components/pages/playerlist/PlayerCard.vue';

const { data: players } = await useFetch('http://localhost:8000/players');

function handlePlayerAdded(newPlayer) {
    players.value.push(newPlayer);
}
</script>

<template>
    <div>
        <v-row>
            <v-col cols="6">
                <h1>メンバー</h1>
            </v-col>
            <v-col cols="6" class="d-flex justify-end">
                <AddButtton @PlayerAdded="handlePlayerAdded" />
            </v-col>
        </v-row>
        <v-row>
            <v-col v-for="(player, i) in players" :key="i" cols="12" md="4">
                <PlayerCard :player="player" />
            </v-col>
        </v-row>
    </div>
</template>
