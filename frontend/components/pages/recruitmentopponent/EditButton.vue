<script setup>
import { shallowRef } from 'vue';

const menu2 = ref(false);
const modal2 = ref(false);
const dialog = shallowRef(false);

const props = defineProps(['recruitment']);
const emit = defineEmits(['recruitmentEdited']);

const recruitmentData = reactive({
    date: props.recruitment.date,
    start_time: props.recruitment.start_time,
    end_time: props.recruitment.end_time,
    location: props.recruitment.location,
});

async function editRecruitment() {
    const updatedRecruitment = await $fetch(
        `http://localhost:8000/recruitments/${props.recruitment.id}`,
        {
            method: 'PUT',
            body: recruitmentData,
        }
    );
    if (updatedRecruitment) {
        // ダイアログを閉じる
        dialog.value = false;
        // イベントを発火して親コンポーネントにプレイヤー情報を渡す
        emit('recruitmentEdited', updatedRecruitment);
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

            <v-card prepend-icon="mdi-form-select" title="募集内容">
                <v-card-text>
                    <v-row>
                        <v-col cols="12" md="5" sm="7"
                            ><v-date-input
                                v-model="recruitmentData.date"
                                label="日付"
                            ></v-date-input>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="11" sm="5">
                            <v-text-field
                                v-model="recruitmentData.start_time"
                                :active="menu2"
                                :focus="menu2"
                                label="開始時刻"
                                prepend-icon="mdi-clock-time-four-outline"
                                readonly
                            >
                                <v-menu
                                    v-model="menu2"
                                    :close-on-content-click="false"
                                    activator="parent"
                                    transition="scale-transition"
                                >
                                    <v-time-picker
                                        v-if="menu2"
                                        format="24hr"
                                        v-model="recruitmentData.start_time"
                                        full-width
                                    ></v-time-picker>
                                </v-menu>
                            </v-text-field>
                        </v-col>

                        <v-col cols="11" sm="5">
                            <v-text-field
                                v-model="recruitmentData.end_time"
                                :active="modal2"
                                :focused="modal2"
                                label="終了時刻"
                                prepend-icon="mdi-clock-time-four-outline"
                                readonly
                            >
                                <v-dialog
                                    v-model="modal2"
                                    activator="parent"
                                    width="auto"
                                >
                                    <v-time-picker
                                        v-if="modal2"
                                        format="24hr"
                                        v-model="recruitmentData.end_time"
                                    ></v-time-picker>
                                </v-dialog>
                            </v-text-field>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12" md="8" sm="6">
                            <v-text-field
                                v-model="recruitmentData.location"
                                hide-details="auto"
                                label="場所"
                                clearable
                                prepend-icon="mdi-map-marker-outline"
                            ></v-text-field>
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
                        @click="editRecruitment"
                    ></v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>
