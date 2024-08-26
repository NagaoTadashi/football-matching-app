<script setup>
import AddButton from '~/components/pages/playerlist/AddButtton.vue';
import PlayerCard from '~/components/pages/playerlist/PlayerCard.vue';

const { data: players } = await useFetch('http://localhost:8000/players');

function handlePlayerAdded(newPlayer) {
    players.value.push(newPlayer);
}

function handlePlayerDeleted(deletedPlayer) {
    players.value = players.value.filter(
        (player) => player.id !== deletedPlayer.id
    );
}
</script>

<template>
    <div>
        <v-row>
            <v-col cols="12" class="d-flex justify-end">
                <AddButton @PlayerAdded="handlePlayerAdded" />
            </v-col>
        </v-row>
        <v-row>
            <v-col v-for="(player, i) in players" :key="i" cols="12" md="4">
                <PlayerCard
                    :player="player"
                    @PlayerDeleted="handlePlayerDeleted"
                />
            </v-col>
        </v-row>
    </div>
</template>
