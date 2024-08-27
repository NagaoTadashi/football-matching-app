<script setup>
import { shallowRef } from 'vue';

const search = shallowRef('');
const games = [
    {
        img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/4.png',
        title: 'レアル・マドリード',
        date: '2024/5/8',
        time: '13:00',
        venue: 'スタジアム',
    },
    {
        img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/2.png',
        title: 'FCバルセロナ',
        date: '2024/5/8',
        time: '13:00',
        venue: 'スタジアム',
    },
    {
        img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/3.png',
        title: 'インテル',
        date: '2024/5/8',
        time: '13:00',
        venue: 'スタジアム',
    },
    {
        img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/5.png',
        title: 'ACミラン',
        date: '2024/5/8',
        time: '13:00',
        venue: 'スタジアム',
    },
    {
        img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/6.png',
        title: 'マンチェスターシティ',
        date: '2024/5/8',
        time: '13:00',
        venue: 'スタジアム',
    },
    {
        img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/7.png',
        title: 'アーセナル',
        date: '2024/5/8',
        time: '13:00',
        venue: 'スタジアム',
    },
    {
        img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/1.png',
        title: 'バイエルン',
        date: '2024/5/8',
        time: '13:00',
        venue: 'スタジアム',
    },
    {
        img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/8.png',
        title: 'リバプール',
        date: '2024/5/8',
        time: '13:00',
        venue: 'スタジアム',
    },
];
</script>

<template>
    <v-card>
        <v-data-iterator :items="games" :items-per-page="3" :search="search">
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
                                        >vs {{ item.raw.title }}</v-card-title
                                    >
                                    <v-card-subtitle>
                                        <v-icon icon="mdi-clock" start></v-icon
                                        >{{ item.raw.date }}
                                        {{ item.raw.time }}</v-card-subtitle
                                    >
                                    <v-card-subtitle>
                                        <v-icon
                                            icon="mdi-map-marker"
                                            start
                                        ></v-icon
                                        >{{ item.raw.venue }}</v-card-subtitle
                                    >
                                </v-card-item>

                                <div class="d-flex justify-space-between px-4">
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

            <template v-slot:footer="{ page, pageCount, prevPage, nextPage }">
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
    </v-card>
</template>
