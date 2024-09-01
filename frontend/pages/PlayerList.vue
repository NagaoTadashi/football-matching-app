<script setup>
import AddButton from '~/components/pages/playerlist/RegisterButtton.vue';
import PlayerCard from '~/components/pages/playerlist/PlayerCard.vue';

const { data: players } = await useFetch('http://localhost:8000/players');

function handlePlayerRegisterd(newPlayer) {
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
        <div v-if="players.length === 0">
            <v-empty-state
                icon="mdi-account"
                title="選手が登録されていません"
            ></v-empty-state>

            <AddButton @PlayerRegisterd="handlePlayerRegisterd" />
        </div>
        <div v-else>
            <v-row>
                <v-col cols="12" class="d-flex justify-end">
                    <AddButton @PlayerRegisterd="handlePlayerRegisterd" />
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
    </div>
</template>
