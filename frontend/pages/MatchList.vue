<script setup>
import { ref } from 'vue';

const color = ref('primary');
const variant = ref('tonal');

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
                <v-card
                    :variant="variant"
                    class="mx-auto"
                    elevation="3"
                    hover
                    link
                    :to="{ name: 'matches-id', params: { id: match.id } }"
                >
                    <v-card-item>
                        <v-card-title>vs {{ match.opponent }}</v-card-title>
                        <v-card-subtitle
                            >日時: {{ match.date }}
                            {{ match.time }}</v-card-subtitle
                        >
                        <v-card-subtitle
                            >場所: {{ match.venue }}</v-card-subtitle
                        >
                        <v-card-subtitle
                            >結果: {{ match.my_team_score }} -
                            {{ match.opponent_score }}</v-card-subtitle
                        >
                    </v-card-item>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>
