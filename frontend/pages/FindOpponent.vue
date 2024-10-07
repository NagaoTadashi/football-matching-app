<script setup>
import { shallowRef } from 'vue';

const user = await getCurrentUser();
const idToken = await user.getIdToken();

const { data: recruitments } = await useFetch(
    'http://localhost:8000/other_team_recruitments',
    {
        method: 'GET',
        headers: {
            Authorization: `Bearer ${idToken}`,
            'Content-Type': 'application/json',
        },
    }
);

const postApplication = async (recruitment_id) => {
    await $fetch('http://localhost:8000/applications', {
        method: 'POST',
        headers: {
            Authorization: `Bearer ${idToken}`,
            'Content-Type': 'application/json',
        },
        body: {
            recruitment_id: recruitment_id,
        },
    });
};

const search = shallowRef('');

const img_url =
    // 'https://images.pexels.com/photos/41257/pexels-photo-41257.jpeg?auto=compress&cs=tinysrgb&w=800';
    // 'https://images.pexels.com/photos/1884574/pexels-photo-1884574.jpeg?auto=compress&cs=tinysrgb&w=800';
    // 'https://images.pexels.com/photos/18420917/pexels-photo-18420917.jpeg?auto=compress&cs=tinysrgb&w=800';
    'https://cdn.pixabay.com/photo/2015/07/02/00/08/football-828218_1280.jpg';

// const tags = [
//     '高校',
//     '大学',
//     '社会人',
//     'Home Improvement',
//     'Vacation',
//     'Food',
//     'Drawers',
//     'Shopping',
//     '8',
//     'Tech',
//     'Creative Writing',
// ];
</script>

<template>
    <div>
        <div
            v-if="recruitments.length === 0"
            class="d-flex align-center justify-center"
            style="min-height: 300px"
        >
            <v-empty-state
                icon="mdi-soccer-field"
                title="申し込み可能な試合がありません"
            >
            </v-empty-state>
        </div>
        <div v-else>
            <v-data-iterator
                :items="games"
                :items-per-page="3"
                :search="search"
            >
                <template v-slot:header>
                    <v-toolbar class="px-2">
                        <v-text-field
                            v-model="search"
                            density="comfortable"
                            placeholder="Search"
                            prepend-inner-icon="mdi-magnify"
                            style="max-width: 300px"
                            variant="solo"
                            clearable
                            hide-details
                        ></v-text-field>
                    </v-toolbar>
                </template>

                <template v-slot:default="{ items }">
                    <v-container class="pa-2" fluid>
                        <v-row>
                            <v-sheet class="py-4 px-1">
                                <v-chip-group
                                    selected-class="text-primary"
                                    multiple
                                >
                                    <v-chip
                                        v-for="tag in tags"
                                        :key="tag"
                                        :text="tag"
                                    ></v-chip>
                                </v-chip-group>
                            </v-sheet>
                        </v-row>
                        <v-row dense>
                            <v-col
                                v-for="item in items"
                                :key="item.title"
                                cols="auto"
                                md="4"
                            >
                                <v-card class="pb-3" border flat>
                                    <v-img :src="item.raw.img"></v-img>

                                    <v-card-item>
                                        <v-card-title
                                            >vs
                                            {{ item.raw.title }}</v-card-title
                                        >
                                        <br />
                                        <v-card-subtitle>
                                            日時：{{ item.raw.date }}
                                            {{ item.raw.time }}</v-card-subtitle
                                        >
                                        <v-card-subtitle>
                                            場所：{{
                                                item.raw.venue
                                            }}</v-card-subtitle
                                        >
                                    </v-card-item>

                                    <div
                                        class="d-flex justify-space-between px-4"
                                    >
                                        <div
                                            class="d-flex align-center text-caption text-medium-emphasis me-1"
                                        ></div>

                                        <v-btn
                                            class="text-none"
                                            size="small"
                                            text="申し込む"
                                            border
                                            flat
                                        >
                                        </v-btn>
                                    </div>
                                </v-card>
                            </v-col>
                        </v-row>
                    </v-container>
                </template>

                <template
                    v-slot:footer="{ page, pageCount, prevPage, nextPage }"
                >
                    <div class="d-flex align-center justify-center pa-4">
                        <v-btn
                            :disabled="page === 1"
                            density="comfortable"
                            icon="mdi-arrow-left"
                            variant="tonal"
                            rounded
                            @click="prevPage"
                        ></v-btn>

                        <div class="mx-2 text-caption">
                            Page {{ page }} of {{ pageCount }}
                        </div>

                        <v-btn
                            :disabled="page >= pageCount"
                            density="comfortable"
                            icon="mdi-arrow-right"
                            variant="tonal"
                            rounded
                            @click="nextPage"
                        ></v-btn>
                    </div>
                </template>
            </v-data-iterator>
        </div>
    </div>
</template>
