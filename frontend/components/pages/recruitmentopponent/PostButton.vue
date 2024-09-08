<script setup>
import { ref, reactive, shallowRef } from 'vue';

const menu2 = ref(false);
const modal2 = ref(false);

const dialog = shallowRef(false);

const emit = defineEmits(['recruitmentPosted']);

const recruitmentData = reactive({
    team_id: 1,
    location: '',
    date: null,
    start_time: null,
    end_time: null,
    status: null,
});

function formatToISODate(date) {
    return new Date(date).toISOString().split('T')[0]; // 日付部分のみ抽出
}

function formatToISOTime(time) {
    const [hours, minutes] = time.split(':');
    const date = new Date();
    date.setHours(hours);
    date.setMinutes(minutes);
    date.setSeconds(0); // 秒の部分を明示的に0に設定
    return date.toISOString().split('T')[1].slice(0, 8); // 'HH:MM:SS' の形式に変換
}

async function postRecruitment() {
    const formattedData = {
        ...recruitmentData,
        date: recruitmentData.date
            ? formatToISODate(recruitmentData.date)
            : null,
        start_time: recruitmentData.start_time
            ? formatToISOTime(recruitmentData.start_time)
            : null,
        end_time: recruitmentData.end_time
            ? formatToISOTime(recruitmentData.end_time)
            : null,
    };

    const newRecruitment = await $fetch('http://localhost:8000/recruitments', {
        method: 'POST',
        body: formattedData,
    });

    // ダイアログを閉じる
    dialog.value = false;
    // イベントを発火して親コンポーネントにプレイヤー情報を渡す
    emit('recruitmentPosted', newRecruitment);
    // フォームデータをクリアする
    recruitmentData.location = '';
    recruitmentData.date = null;
    recruitmentData.start_time = null;
    recruitmentData.end_time = null;
}
</script>

<template>
    <div class="pa-4 text-center">
        <v-dialog v-model="dialog" max-width="600">
            <template v-slot:activator="{ props: activatorProps }">
                <v-btn
                    class="text-none font-weight-regular"
                    prepend-icon="mdi-text-box-plus-outline"
                    text="募集を投稿"
                    variant="tonal"
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
                        text="投稿"
                        variant="tonal"
                        @click="postRecruitment"
                    ></v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>
