<script setup>
import { ref } from 'vue';
import EditButton from './EditButton.vue';
import DeleteButton from './DeleteButton.vue';

const props = defineProps(['player']);

const variant = ref('tonal');

const emit = defineEmits(['playerDeleted']);

function handlePlayerDeleted(deletedPlayer) {
    emit('playerDeleted', deletedPlayer);
}

function handlePlayerEdited(updatedPlayer) {
    Object.assign(props.player, updatedPlayer);
}
</script>

<template>
    <v-card :variant="variant" class="mx-auto" elevation="5">
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
                <v-row>
                    <EditButton
                        :player="player"
                        @playerEdited="handlePlayerEdited"
                    />
                </v-row>
                <v-row>
                    <DeleteButton
                        :player="player"
                        @playerDeleted="handlePlayerDeleted"
                    />
                </v-row>
            </v-col>
        </v-row>
    </v-card>
</template>
