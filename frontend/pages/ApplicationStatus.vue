<script setup>
import { ref } from 'vue';

const user = await getCurrentUser();
const idToken = await user.getIdToken();

const { data: applications } = await useFetch(
    'http://localhost:8000/application_status',
    {
        method: 'GET',
        headers: {
            Authorization: `Bearer ${idToken}`,
            'Content-Type': 'application/json',
        },
    }
);

const itemId = ref(-1);
const dialog = ref(false);
const dialogDelete = ref(false);
const headers = ref([
    { title: '状態', align: 'start', key: 'status', sortable: false },
    { title: 'チーム', key: 'name', sortable: false },
    { title: '年', key: 'year', sortable: false },
    { title: '月', key: 'month', sortable: false },
    { title: '日', key: 'day', sortable: false },
    { title: '開始', key: 'start_time', sortable: false },
    { title: '終了', key: 'end_time', sortable: false },
    { title: '場所', key: 'location', sortable: false },
    { title: '', key: 'actions', sortable: false },
]);

async function deleteApplication(id) {
    await $fetch(`http://localhost:8000/application/${id}`, {
        method: 'DELETE',
    });

    applications.value = applications.value.filter(
        (application) => application.id !== id
    );
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
    deleteApplication(itemId.value);
    closeDelete();
}

watch(dialogDelete, (val) => {
    val || closeDelete();
});
</script>

<template>
    <div>
        <v-data-table
            :headers="headers"
            :items="applications"
            :sort-by="[
                { key: 'year', order: 'desc' },
                { key: 'month', order: 'desc' },
                { key: 'day', order: 'desc' },
            ]"
        >
            <template v-slot:top>
                <v-toolbar flat>
                    <v-toolbar-title>申し込み状況</v-toolbar-title>
                    <v-divider class="mx-4" inset vertical></v-divider>
                    <v-spacer></v-spacer>
                    <v-dialog v-model="dialogDelete" max-width="550px">
                        <v-card
                            prepend-icon="mdi-alert-circle-outline"
                            title="この申し込みをキャンセルしてもよろしいですか？"
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
                    v-tooltip:top="'キャンセル'"
                >
                    mdi-cancel
                </v-icon>
            </template>
            <template v-slot:no-data>申し込みはまだありません</template>
        </v-data-table>
    </div>
</template>
