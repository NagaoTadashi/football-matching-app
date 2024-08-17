<script setup>
import MatchCard from '~/components/pages/matchlist/MatchCard.vue';

const { data: matches } = await useFetch('http://localhost:8000/matches');
</script>
<template>
    <div>
        <v-row>
            <v-col cols="6">
                <h1>試合日程・結果</h1>
            </v-col>
        </v-row>
        <v-row>
            <v-col v-for="(match, i) in matches" :key="i" cols="12" md="4">
                <MatchCard :match="match" />
            </v-col>
        </v-row>
    </div>
</template>
