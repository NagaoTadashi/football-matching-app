<script setup>
import AddButtton from '../components/pages/memberlist/AddButtton.vue';
import PlayerCard from '~/components/pages/memberlist/PlayerCard.vue';

const { data: member } = await useFetch('http://localhost:8000/member');
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
