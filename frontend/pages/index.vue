<script setup>
import { ref } from 'vue';
import AddButton from '~/components/pages/index/playerlist/AddButtton.vue';
import PlayerCard from '~/components/pages/index/playerlist/PlayerCard.vue';

const { data: players } = await useFetch('http://localhost:8000/players');

function handlePlayerAdded(newPlayer) {
    players.value.push(newPlayer);
}

function handlePlayerDeleted(deletedPlayer) {
    players.value = players.value.filter(
        (player) => player.id !== deletedPlayer.id
    );
}

const tab = ref(null);
</script>

<template>
    <div>
        <v-tabs v-model="tab" align-tabs="center" color="deep-purple-accent-4">
            <v-tab :value="1">基本情報</v-tab>
            <v-tab :value="2">選手一覧</v-tab>
        </v-tabs>

        <v-tabs-window v-model="tab">
            <v-tabs-window-item :value="1">
                <h1>チーム写真</h1>
                <h1>所属リーグ</h1>
                <h1>活動日</h1>
                <h1>所在地</h1></v-tabs-window-item
            >
            <v-tabs-window-item :value="2">
                <v-container fluid>
                    <v-row>
                        <v-col cols="12" class="d-flex justify-end">
                            <AddButton @PlayerAdded="handlePlayerAdded" />
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col
                            v-for="(player, i) in players"
                            :key="i"
                            cols="12"
                            md="4"
                        >
                            <PlayerCard
                                :player="player"
                                @PlayerDeleted="handlePlayerDeleted"
                            />
                        </v-col>
                    </v-row>
                </v-container>
            </v-tabs-window-item>
        </v-tabs-window>
    </div>
</template>
