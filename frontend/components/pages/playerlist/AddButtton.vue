<script setup>
import { reactive, shallowRef } from 'vue';
import { VNumberInput } from 'vuetify/labs/VNumberInput';

const dialog = shallowRef(false);
const positions = ['GK', 'DF', 'MF', 'FW'];

const emit = defineEmits(['PlayerAdded']);

const playerData = reactive({
    position: '',
    number: null,
    name: '',
    namae: '',
});

async function addPlayer() {
    const newPlayer = await $fetch('http://localhost:8000/player', {
        method: 'POST',
        body: playerData,
    });
    // ダイアログを閉じる
    dialog.value = false;
    // イベントを発火して親コンポーネントにプレイヤー情報を渡す
    emit('playerAdded', newPlayer);
    // フォームデータをクリアする
    playerData.position = '';
    playerData.number = null;
    playerData.name = '';
    playerData.namae = '';
}
</script>

<template>
    <div class="pa-4 text-center">
        <v-dialog v-model="dialog" max-width="600">
            <template v-slot:activator="{ props: activatorProps }">
                <v-btn
                    class="text-none font-weight-regular"
                    prepend-icon="mdi-plus"
                    text="選手を追加"
                    variant="tonal"
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
                        text="登録"
                        variant="tonal"
                        @click="addPlayer"
                    ></v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>
