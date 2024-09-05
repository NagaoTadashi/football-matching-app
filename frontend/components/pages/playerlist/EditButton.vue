<script setup>
import { shallowRef } from 'vue';
import { VNumberInput } from 'vuetify/labs/VNumberInput';

const dialog = shallowRef(false);
const positions = ['GK', 'DF', 'MF', 'FW'];

const props = defineProps(['player']);
const emit = defineEmits(['PlayerEdited']);

const playerData = reactive({
    position: props.player.position,
    number: props.player.number,
    namae: props.player.namae,
    name: props.player.name,
});

async function editPlayer() {
    const updatedPlayer = await $fetch(
        `http://localhost:8000/players/${props.player.id}`,
        {
            method: 'PUT',
            body: playerData,
        }
    );
    if (updatedPlayer) {
        // ダイアログを閉じる
        dialog.value = false;
        // イベントを発火して親コンポーネントにプレイヤー情報を渡す
        emit('PlayerEdited', updatedPlayer);
    }
}
</script>

<template>
    <div class="pa-4 text-center">
        <v-dialog v-model="dialog" max-width="600">
            <template v-slot:activator="{ props: activatorProps }">
                <v-btn
                    class="text-none font-weight-regular"
                    text="編集"
                    elevation="5"
                    v-bind="activatorProps"
                ></v-btn>
            </template>

            <v-card prepend-icon="mdi-account" title="選手情報">
                <v-card-text>
                    <v-row dense>
                        <v-col cols="12" md="4" sm="6">
                            <v-select
                                v-model="playerData.position"
                                :items="positions"
                                label="ポジション"
                            ></v-select
                        ></v-col>
                        <v-col cols="12" md="4" sm="6"
                            ><v-number-input
                                v-model="playerData.number"
                                label="背番号"
                                control-variant="stacked"
                            ></v-number-input
                        ></v-col>
                    </v-row>
                    <v-row dense>
                        <v-col>
                            <v-responsive class="mx-auto" max-width="344">
                                <v-text-field
                                    v-model="playerData.namae"
                                    hide-details="auto"
                                    label="名前"
                                    clearable
                                ></v-text-field>
                            </v-responsive>
                        </v-col>
                        <v-col>
                            <v-responsive class="mx-auto" max-width="344">
                                <v-text-field
                                    v-model="playerData.name"
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
                        text="キャンセル"
                        variant="plain"
                        @click="dialog = false"
                    ></v-btn>

                    <v-btn
                        color="primary"
                        text="保存"
                        variant="tonal"
                        @click="editPlayer"
                    ></v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>
