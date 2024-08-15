<script setup>
import { ref } from 'vue';

const matches = {
    match1: {
        id: 1,
        opponent: 'チームA',
        date: '1999/5/8',
        time: '12:00',
        venue: 'Aグラウンド',
        score: '-',
    },
    match2: {
        id: 2,
        opponent: 'チームB',
        date: '1999/5/8',
        time: '12:00',
        venue: 'Bグラウンド',
        score: '○3-0',
    },
    match3: {
        id: 3,
        opponent: 'チームC',
        date: '1999/5/8',
        time: '12:00',
        venue: 'Cグラウンド',
        score: '○6-0',
    },
    match4: {
        id: 4,
        opponent: 'チームD',
        date: '1999/5/8',
        time: '12:00',
        venue: 'Dグラウンド',
        score: '●0-10',
    },
    match5: {
        id: 5,
        opponent: 'チームE',
        date: '1999/5/8',
        time: '12:00',
        venue: 'Eグラウンド',
        score: '△1-1',
    },
    match6: {
        id: 6,
        opponent: 'チームF',
        date: '1999/5/8',
        time: '12:00',
        venue: 'Fグラウンド',
        score: '○1-0',
    },
    match7: {
        id: 7,
        opponent: 'チームG',
        date: '1999/5/8',
        time: '12:00',
        venue: 'Gグラウンド',
        score: '●0-10',
    },
    match8: {
        id: 8,
        opponent: 'チームH',
        date: '1999/5/8',
        time: '12:00',
        venue: 'Hグラウンド',
        score: '△1-1',
    },
    match9: {
        id: 9,
        opponent: 'チームI',
        date: '1999/5/8',
        time: '12:00',
        venue: 'Iグラウンド',
        score: '○1-0',
    },
};

const color = ref('primary');
const variant = ref('tonal');
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
                            >結果: {{ match.score }}</v-card-subtitle
                        >
                    </v-card-item>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>
