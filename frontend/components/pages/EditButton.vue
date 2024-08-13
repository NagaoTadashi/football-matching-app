<script setup>
import { ref, shallowRef } from 'vue';
import { VNumberInput } from 'vuetify/labs/VNumberInput';

defineProps(['player']);

const dialog = shallowRef(false);
const positions = ['GK', 'DF', 'MF', 'FW'];
</script>

<template>
    <div class="pa-4 text-center">
        <v-dialog v-model="dialog" max-width="600">
            <template v-slot:activator="{ props: activatorProps }">
                <v-btn
                    class="text-none font-weight-regular"
                    prepend-icon="mdi-account"
                    text="Edit"
                    variant="tonal"
                    v-bind="activatorProps"
                ></v-btn>
            </template>

            <v-card prepend-icon="mdi-account" title="Player Profile">
                <v-card-text>
                    <v-row dense>
                        <v-col cols="12" md="4" sm="6">
                            <v-select
                                :items="positions"
                                label="ポジション"
                                v-model="player.position"
                            ></v-select
                        ></v-col>
                        <v-col cols="12" md="4" sm="6"
                            ><v-number-input
                                label="背番号"
                                control-variant="stacked"
                            ></v-number-input
                        ></v-col>
                    </v-row>
                    <v-row dense>
                        <v-col>
                            <v-responsive class="mx-auto" max-width="344">
                                <v-text-field
                                    v-model="player.namae"
                                    hide-details="auto"
                                    label="名前"
                                    clearable
                                ></v-text-field>
                            </v-responsive>
                        </v-col>
                        <v-col>
                            <v-responsive class="mx-auto" max-width="344">
                                <v-text-field
                                    v-model="player.name"
                                    hide-details="auto"
                                    label="name"
                                    clearable
                                ></v-text-field>
                            </v-responsive>
                        </v-col>
                    </v-row>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                    <v-spacer></v-spacer>

                    <v-btn
                        text="Close"
                        variant="plain"
                        @click="dialog = false"
                    ></v-btn>

                    <v-btn
                        color="primary"
                        text="Save"
                        variant="tonal"
                        @click="dialog = false"
                    ></v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>
