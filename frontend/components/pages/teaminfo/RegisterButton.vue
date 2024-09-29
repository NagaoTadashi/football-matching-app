<script setup>
import { ref, shallowRef } from 'vue';

const props = defineProps(['idToken']);

const dialog = shallowRef(false);

const teamInfo = ref({
    name: '',
    region: '',
    prefecture: '',
    category: '',
    league: '',
});

const regions = {
    '北海道・東北': [
        '北海道',
        '青森県',
        '岩手県',
        '宮城県',
        '秋田県',
        '山形県',
        '福島県',
    ],
    関東: [
        '茨城県',
        '栃木県',
        '群馬県',
        '埼玉県',
        '千葉県',
        '東京都',
        '神奈川県',
    ],
    中部: [
        '新潟県',
        '富山県',
        '石川県',
        '福井県',
        '山梨県',
        '長野県',
        '岐阜県',
        '静岡県',
        '愛知県',
    ],
    近畿: [
        '三重県',
        '滋賀県',
        '京都府',
        '大阪府',
        '兵庫県',
        '奈良県',
        '和歌山県',
    ],
    中国: ['鳥取県', '島根県', '岡山県', '広島県', '山口県'],
    四国: ['徳島県', '香川県', '愛媛県', '高知県'],
    '九州・沖縄': [
        '福岡県',
        '佐賀県',
        '長崎県',
        '熊本県',
        '大分県',
        '宮崎県',
        '鹿児島県',
        '沖縄県',
    ],
};

const regionsList = Object.keys(regions);

const category = ['社会人', '大学', '高校', '中学', '小学'];

const emit = defineEmits(['teamInfoRegisterd']);

async function registerTeamInfo() {
    const newTeamInfo = await $fetch('http://localhost:8000/team_info', {
        method: 'POST',
        headers: {
            Authorization: `Bearer ${props.idToken}`,
            'Content-Type': 'application/json',
        },
        body: teamInfo.value,
    });
    // ダイアログを閉じる
    dialog.value = false;
    // イベントを発火して親コンポーネントにチーム情報を渡す
    emit('teamInfoRegisterd', newTeamInfo);
    // フォームデータをクリアする
    teamInfo.value.name = '';
    teamInfo.value.region = '';
    teamInfo.value.prefecture = '';
    teamInfo.value.category = '';
    teamInfo.value.league = '';
}

const isValid = computed(() => {
    return (
        teamInfo.value.name &&
        teamInfo.value.region &&
        teamInfo.value.prefecture &&
        teamInfo.value.category &&
        teamInfo.value.league
    );
});

function required(v) {
    return !!v || 'フィールドは必須です';
}
</script>

<template>
    <div class="pa-4 text-center">
        <v-dialog v-model="dialog" max-width="600">
            <template v-slot:activator="{ props: activatorProps }">
                <v-btn
                    class="text-none font-weight-regular"
                    prepend-icon="mdi-plus"
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
                                v-model="teamInfo.name"
                                label="チーム名を入力"
                                :rules="[required]"
                                clearable
                            ></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12" md="4" sm="6">
                            <v-select
                                v-model="teamInfo.region"
                                :items="regionsList"
                                label="地域を選択"
                                :rules="[required]"
                            ></v-select>
                        </v-col>
                        <v-col cols="12" md="4" sm="6">
                            <v-select
                                v-model="teamInfo.prefecture"
                                :items="regions[teamInfo.region]"
                                label="都道府県を選択"
                                :rules="[required]"
                            ></v-select>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12" md="4" sm="6">
                            <v-select
                                v-model="teamInfo.category"
                                :items="category"
                                label="カテゴリを選択"
                                :rules="[required]"
                            ></v-select>
                        </v-col>
                        <v-col cols="12" md="8" sm="6">
                            <v-text-field
                                v-model="teamInfo.league"
                                label="所属リーグを入力"
                                :rules="[required]"
                                clearable
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
                        :disabled="!isValid"
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
