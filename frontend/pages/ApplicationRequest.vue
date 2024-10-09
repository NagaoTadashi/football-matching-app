<script setup>
import { ref } from 'vue';

const user = await getCurrentUser();
const idToken = await user.getIdToken();

const { data: applicationRequests } = await useFetch(
    'http://localhost:8000/application_requests',
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
    { title: 'チーム', align: 'start', key: 'name', sortable: false },
    { title: '年', key: 'year', sortable: false },
    { title: '月', key: 'month', sortable: false },
    { title: '日', key: 'day', sortable: false },
    { title: '開始', key: 'start_time', sortable: false },
    { title: '終了', key: 'end_time', sortable: false },
    { title: '場所', key: 'location', sortable: false },
    { title: 'Actions', key: 'actions', sortable: false },
]);
</script>

<template>
    <div>
        <v-data-table
            :headers="headers"
            :items="applicationRequests"
            :sort-by="[
                { key: 'year', order: 'desc' },
                { key: 'month', order: 'desc' },
                { key: 'day', order: 'desc' },
            ]"
        >
            <template v-slot:top>
                <v-toolbar flat>
                    <v-toolbar-title
                        >他チームからの申し込み依頼</v-toolbar-title
                    >
                </v-toolbar>
            </template>
            <template v-slot:[`item.actions`]="{ item }">
                <v-icon
                    class="me-2"
                    color="#4CAF50"
                    @click="editItem(item)"
                    v-tooltip:top="'承認'"
                >
                    mdi-check-circle-outline
                </v-icon>
                <v-icon
                    color="#F44336"
                    class="me-2"
                    @click="deleteItem(item)"
                    v-tooltip:top="'拒否'"
                >
                    mdi-close-circle
                </v-icon>
            </template>
            <template v-slot:no-data>
                他チームからの申し込みはまだありません
            </template>
        </v-data-table>
    </div>
</template>
