<script setup>
import EditButton from '~/components/pages/playerlist/EditButton.vue';

const props = defineProps(['player']);

const variant = ref('tonal');

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
                <EditButton
                    :player="player"
                    @PlayerEdited="handlePlayerEdited"
                />
            </v-col>
        </v-row>
    </v-card>
</template>
