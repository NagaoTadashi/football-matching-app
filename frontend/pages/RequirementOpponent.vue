<script setup>
import { nextTick, ref, watch } from 'vue';

const user = await getCurrentUser();
const idToken = await user.getIdToken();

const { data: teamInfo } = await useFetch('http://localhost:8000/team_info', {
    method: 'GET',
    headers: {
        Authorization: `Bearer ${idToken}`,
        'Content-Type': 'application/json',
    },
});

const { data: recruitments } = await useFetch(
    'http://localhost:8000/my_team_recruitments',
    {
        method: 'GET',
        headers: {
            Authorization: `Bearer ${idToken}`,
            'Content-Type': 'application/json',
        },
    }
);

const dialog = ref(false);
const dialogDelete = ref(false);
const headers = ref([
    { title: '状態', align: 'start', key: 'status' },
    { title: '年', key: 'year', sortable: false },
    { title: '月', key: 'month', sortable: false },
    { title: '日', key: 'day', sortable: false },
    { title: '開始', key: 'start_time', sortable: false },
    { title: '終了', key: 'end_time', sortable: false },
    { title: '場所', key: 'location', sortable: false },
    { title: '', key: 'actions', sortable: false },
]);

const itemId = ref(-1);
const editedItem = ref({
    year: null,
    month: null,
    day: null,
    start_time: '',
    end_time: '',
    location: '',
});
const defaultItem = ref({
    year: null,
    month: null,
    day: null,
    start_time: '',
    end_time: '',
    location: '',
});

async function postRecruitment() {
    const postedRecruitment = await $fetch(
        'http://localhost:8000/recruitments',
        {
            method: 'POST',
            headers: {
                Authorization: `Bearer ${idToken}`,
                'Content-Type': 'application/json',
            },
            body: editedItem.value,
        }
    );
    recruitments.value.push(postedRecruitment);
}

async function deleteRecruitment(id) {
    await $fetch(`http://localhost:8000/recruitments/${id}`, {
        method: 'DELETE',
    });

    recruitments.value = recruitments.value.filter(
        (recruitment) => recruitment.id !== id
    );
}

function close() {
    dialog.value = false;
    nextTick(() => {
        editedItem.value = Object.assign({}, defaultItem.value);
        itemId.value = -1;
    });
}

function post() {
    postRecruitment();
    close();
}

function deleteItem(item) {
    itemId.value = item.id;
    dialogDelete.value = true;
}

function closeDelete() {
    dialogDelete.value = false;
    nextTick(() => {
        itemId.value = -1;
    });
}

function deleteItemConfirm() {
    deleteRecruitment(itemId.value);
    closeDelete();
}

const currentYear = new Date().getFullYear();
const yearOptions = [currentYear, currentYear + 1];

const monthOptions = Array.from({ length: 12 }, (_, i) => i + 1);

const dayOptions = Array.from({ length: 31 }, (_, i) => i + 1);

// 1時間間隔で時間を生成する関数
const generateTimeOptions = () => {
    const times = [];
    for (let hour = 0; hour < 24; hour++) {
        // 時間を "HH:00" 形式にフォーマット
        const formattedTime = `${String(hour).padStart(2, '0')}:00`;
        times.push(formattedTime);
    }
    return times;
};

const timeOptions = generateTimeOptions();

watch(dialog, (val) => {
    val || close();
});
watch(dialogDelete, (val) => {
    val || closeDelete();
});

const isValid = computed(() => {
    return (
        editedItem.value.year &&
        editedItem.value.month &&
        editedItem.value.day &&
        editedItem.value.start_time &&
        editedItem.value.end_time &&
        editedItem.value.location
    );
});
</script>

<template>
    <div v-if="teamInfo === null">
        <v-empty-state
            class="d-flex align-center justify-center"
            style="min-height: 300px"
            icon="mdi-tshirt-crew"
            title="チーム情報が登録されていません"
        >
            <template #text>
                「<v-icon left>mdi-tshirt-crew</v-icon>
                チーム情報」より、まずはじめにチーム情報を登録してください
            </template>
        </v-empty-state>
    </div>
    <div v-else>
        <v-data-table
            :headers="headers"
            :items="recruitments"
            :sort-by="[
                { key: 'year', order: 'desc' },
                { key: 'month', order: 'desc' },
                { key: 'day', order: 'desc' },
            ]"
        >
            <template v-slot:top>
                <v-toolbar flat>
                    <v-toolbar-title>投稿済みの募集一覧</v-toolbar-title>
                    <v-divider class="mx-4" inset vertical></v-divider>
                    <v-spacer></v-spacer>

                    <v-btn
                        prepend-icon="mdi-text-box-plus-outline"
                        elevation="5"
                        @click="dialog = true"
                    >
                        募集を投稿
                    </v-btn>

                    <v-dialog v-model="dialog" max-width="500px">
                        <v-card prepend-icon="mdi-form-select" title="募集内容">
                            <v-card-text>
                                <v-container>
                                    <v-row>
                                        <v-col class="d-flex align-center">
                                            <v-icon>
                                                mdi-calendar-month
                                            </v-icon>
                                        </v-col>
                                        <v-col md="4" sm="7">
                                            <v-select
                                                v-model="editedItem.year"
                                                label="年"
                                                :items="yearOptions"
                                            />
                                        </v-col>
                                        <v-col md="3" sm="7">
                                            <v-select
                                                v-model="editedItem.month"
                                                label="月"
                                                :items="monthOptions"
                                            />
                                        </v-col>
                                        <v-col md="3" sm="7">
                                            <v-select
                                                v-model="editedItem.day"
                                                label="日"
                                                :items="dayOptions"
                                            />
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col class="d-flex align-center">
                                            <v-icon>
                                                mdi-clock-time-eight-outline
                                            </v-icon>
                                        </v-col>
                                        <v-col cols="5" md="5" sm="7">
                                            <v-select
                                                v-model="editedItem.start_time"
                                                label="開始時間"
                                                :items="timeOptions"
                                            />
                                        </v-col>
                                        <v-col cols="5" md="5" sm="7">
                                            <v-select
                                                v-model="editedItem.end_time"
                                                label="終了時間"
                                                :items="timeOptions"
                                            />
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col class="d-flex align-center">
                                            <v-icon>
                                                mdi-map-marker-outline</v-icon
                                            >
                                        </v-col>
                                        <v-col cols="12" md="10" sm="7">
                                            <v-text-field
                                                v-model="editedItem.location"
                                                hide-details="auto"
                                                label="場所"
                                                clearable
                                            ></v-text-field>
                                        </v-col>
                                    </v-row>
                                </v-container>
                            </v-card-text>

                            <v-divider></v-divider>

                            <v-card-actions>
                                <v-spacer></v-spacer>

                                <v-btn
                                    text="キャンセル"
                                    variant="plain"
                                    @click="close"
                                >
                                </v-btn>

                                <v-btn
                                    color="primary"
                                    text="投稿"
                                    variant="tonal"
                                    @click="post"
                                    :disabled="!isValid"
                                >
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                    <v-dialog v-model="dialogDelete" max-width="500px">
                        <v-card
                            prepend-icon="mdi-alert-circle-outline"
                            title="この募集投稿を削除してもよろしいですか？"
                        >
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn
                                    text="キャンセル"
                                    variant="plain"
                                    @click="closeDelete"
                                ></v-btn>
                                <v-btn
                                    color="primary"
                                    text="OK"
                                    variant="tonal"
                                    @click="deleteItemConfirm"
                                ></v-btn>
                                <v-spacer></v-spacer>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </v-toolbar>
            </template>
            <template v-slot:[`item.actions`]="{ item }">
                <v-icon
                    color="#F44336"
                    class="me-2"
                    @click="deleteItem(item)"
                    v-tooltip:top="'削除'"
                >
                    mdi-delete
                </v-icon>
            </template>
            <template v-slot:no-data> 募集が投稿されていません </template>
        </v-data-table>
    </div>
</template>
