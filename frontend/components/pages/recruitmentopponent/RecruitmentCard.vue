<script setup>
import { ref } from 'vue';
import { format } from 'date-fns';
import EditButton from './EditButton.vue';
import DeleteButton from './DeleteButton.vue';

const props = defineProps(['recruitment']);

const variant = ref('tonal');

const emit = defineEmits(['recruitmentDeleted']);

function handleRecruitmentDeleted(deletedRecruitment) {
    emit('recruitmentDeleted', deletedRecruitment);
}

function handleRecruitmentEdited(updatedRecruitment) {
    Object.assign(props.recruitment, updatedRecruitment);
}
</script>

<template>
    <v-card :variant="variant" class="mx-auto" elevation="5">
        <v-card-item>
            <v-card-title>{{ recruitment.status }}</v-card-title>
            <v-card-subtitle
                ><v-icon size="18">mdi-calendar</v-icon>
                {{ recruitment.date }}
            </v-card-subtitle>
            <v-card-subtitle>
                <v-icon size="18">mdi-clock-time-four-outline</v-icon>
                {{
                    format(
                        new Date(`1970-01-01T${recruitment.start_time}Z`),
                        'HH:mm'
                    )
                }}
                ~
                {{
                    format(
                        new Date(`1970-01-01T${recruitment.end_time}Z`),
                        'HH:mm'
                    )
                }}
            </v-card-subtitle>
            <v-card-subtitle
                ><v-icon size="18">mdi-map-marker-outline</v-icon>
                {{ recruitment.location }}</v-card-subtitle
            >
        </v-card-item>
        <v-card-actions class="d-flex align-center justify-center">
            <EditButton
                :recruitment="recruitment"
                @recruitmentEdited="handleRecruitmentEdited"
            />

            <DeleteButton
                :recruitment="recruitment"
                @recruitmentDeleted="handleRecruitmentDeleted"
            />
        </v-card-actions>
    </v-card>
</template>
