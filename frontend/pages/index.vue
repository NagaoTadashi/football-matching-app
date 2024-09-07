<script setup>
import MatchCard from '~/components/pages/matchlist/MatchCard.vue';

const { data: matches } = await useFetch('http://localhost:8000/matches');
</script>

<template>
    <div
        v-if="matches.length === 0"
        class="d-flex align-center justify-center"
        style="min-height: 300px"
    >
        <v-empty-state
            icon="mdi-soccer-field"
            title="試合日程・結果はまだありません"
        >
        </v-empty-state>
    </div>
    <div v-else>
        <v-row>
            <v-col v-for="(match, i) in matches" :key="i" cols="12" md="4">
                <MatchCard :match="match" />
            </v-col>
        </v-row>
    </div>
</template>
