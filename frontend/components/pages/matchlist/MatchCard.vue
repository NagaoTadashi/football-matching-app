<script setup>
import { ref } from 'vue';

defineProps(['match']);

const variant = ref('tonal');
</script>

<template>
    <v-card
        :variant="variant"
        class="mx-auto"
        elevation="5"
        hover
        link
        :to="{ name: 'matches-id', params: { id: match.id } }"
    >
        <v-card-item>
            <v-card-title>vs {{ match.opponent }}</v-card-title>
            <v-card-subtitle
                >日時: {{ match.date }} {{ match.time }}</v-card-subtitle
            >
            <v-card-subtitle>場所: {{ match.venue }}</v-card-subtitle>
            <v-card-subtitle
                >結果: {{ match.my_team_score }} -
                {{ match.opponent_score }}</v-card-subtitle
            >
        </v-card-item>
    </v-card>
</template>
