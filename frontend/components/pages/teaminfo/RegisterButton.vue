<script setup>
import { reactive, shallowRef } from 'vue';

const dialog = shallowRef(false);
const region = [
    '北海道',
    '青森県',
    '岩手県',
    '宮城県',
    '秋田県',
    '山形県',
    '福島県',
    '茨城県',
    '栃木県',
    '群馬県',
    '埼玉県',
    '千葉県',
    '東京都',
    '神奈川県',
    '新潟県',
    '富山県',
    '石川県',
    '福井県',
    '山梨県',
    '長野県',
    '岐阜県',
    '静岡県',
    '愛知県',
    '三重県',
    '滋賀県',
    '京都府',
    '大阪府',
    '兵庫県',
    '奈良県',
    '和歌山県',
    '鳥取県',
    '島根県',
    '岡山県',
    '広島県',
    '山口県',
    '徳島県',
    '香川県',
    '愛媛県',
    '高知県',
    '福岡県',
    '佐賀県',
    '長崎県',
    '熊本県',
    '大分県',
    '宮崎県',
    '鹿児島県',
    '沖縄県',
];
const category = ['社会人', '大学', '高校', '中学', '小学'];

const emit = defineEmits(['TeamInfoRegisterd']);

const teamInfo = reactive({
    name: '',
    region: '',
    category: '',
    league: '',
});

async function registerTeamInfo() {
    const newTeamInfo = await $fetch('http://localhost:8000/team_info', {
        method: 'POST',
        body: teamInfo,
    });
    // ダイアログを閉じる
    dialog.value = false;
    // イベントを発火して親コンポーネントにチーム情報を渡す
    emit('TeamInfoRegisterd', newTeamInfo);
    // フォームデータをクリアする
    teamInfo.name = '';
    teamInfo.region = '';
    teamInfo.category = '';
    teamInfo.league = '';
}
</script>

<template>
    <div class="pa-4 text-center">
        <v-dialog v-model="dialog" max-width="600">
            <template v-slot:activator="{ props: activatorProps }">
                <v-btn
                    class="text-none font-weight-regular"
                    text="チーム情報を登録"
                    variant="tonal"
                    elevation="5"
                    v-bind="activatorProps"
                ></v-btn>
            </template>

            <v-card prepend-icon="mdi-tshirt-crew" title="チーム情報">
                <v-card-text>
                    <v-row dense>
                        <v-col cols="12" md="6" sm="6">
                            <v-text-field
                                label="チーム名"
                                v-model="teamInfo.name"
                            ></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12" md="3" sm="6">
                            <v-select
                                :items="region"
                                density="default"
                                label="地域"
                                v-model="teamInfo.region"
                            ></v-select>
                        </v-col>
                        <v-col cols="12" md="4" sm="6">
                            <v-select
                                :items="category"
                                density="default"
                                label="カテゴリ"
                                v-model="teamInfo.category"
                            ></v-select>
                        </v-col>
                        <v-col cols="12" md="8" sm="6">
                            <v-text-field
                                label="所属リーグ"
                                v-model="teamInfo.league"
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
                        text="登録"
                        variant="tonal"
                        @click="registerTeamInfo"
                    ></v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>
