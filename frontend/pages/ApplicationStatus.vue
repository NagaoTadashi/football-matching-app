<script setup>
import { ref } from 'vue';

const user = await getCurrentUser();
const idToken = await user.getIdToken();

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
    { title: '状態', align: 'start', key: 'status', sortable: false },
    { title: 'チーム', key: 'name', sortable: false },
    { title: '年', key: 'year', sortable: false },
    { title: '月', key: 'month', sortable: false },
    { title: '日', key: 'day', sortable: false },
    { title: '開始', key: 'start_time', sortable: false },
    { title: '終了', key: 'end_time', sortable: false },
    { title: '場所', key: 'location', sortable: false },
]);
</script>

<template>
    <div>
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
                    <v-toolbar-title>申し込み状況</v-toolbar-title>
                </v-toolbar>
            </template>

            <template v-slot:no-data>申し込みはまだありません</template>
        </v-data-table>
    </div>
</template>
