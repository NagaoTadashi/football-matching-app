<script setup>
import EditButton from '~/components/pages/EditButton.vue';
defineProps(['player']);

const color = ref('primary');
const variant = ref('tonal');
</script>

<template>
    <v-card :variant="variant" class="mx-auto" elevation="3">
        <v-row>
            <v-col>
                <v-card-item>
                    <v-card-title
                        >{{ player.position }} {{ player.number }}</v-card-title
                    >
                    <v-card-title>{{ player.namae }}</v-card-title>
                    <v-card-subtitle>{{ player.name }} </v-card-subtitle>
                </v-card-item>
            </v-col>
            <v-col class="d-flex align-end justify-end">
                <EditButton :player="player" />
            </v-col>
        </v-row>
    </v-card>
</template>
