<script setup>
const user = await getCurrentUser();
const idToken = await user.getIdToken();

const runtimeConfig = useRuntimeConfig();

const { data: matches } = await useFetch(
    `${runtimeConfig.public.apiUrl}/matches`,
    {
        method: 'GET',
        headers: {
            Authorization: `Bearer ${idToken}`,
            'Content-Type': 'application/json',
        },
    }
);

const { data: myTeam } = await useFetch(
    `${runtimeConfig.public.apiUrl}/team_info`,
    {
        method: 'GET',
        headers: {
            Authorization: `Bearer ${idToken}`,
            'Content-Type': 'application/json',
        },
    }
);

const search = shallowRef('');

const img_url =
    // 'https://images.pexels.com/photos/41257/pexels-photo-41257.jpeg?auto=compress&cs=tinysrgb&w=800';
    // 'https://images.pexels.com/photos/1884574/pexels-photo-1884574.jpeg?auto=compress&cs=tinysrgb&w=800';
    // 'https://images.pexels.com/photos/18420917/pexels-photo-18420917.jpeg?auto=compress&cs=tinysrgb&w=800';
    'https://cdn.pixabay.com/photo/2015/07/02/00/08/football-828218_1280.jpg';
</script>

<template>
    <div>
        <div
            v-if="matches.length === 0"
            class="d-flex align-center justify-center"
            style="min-height: 300px"
        >
            <v-empty-state
                icon="mdi-soccer-field"
                title="試合日程・結果はまだありません"
            >
            </v-empty-state>
        </div>
        <div v-else>
            <v-data-iterator
                :items="matches"
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
                        <v-row dense>
                            <v-col
                                v-for="item in items"
                                :key="item.title"
                                cols="auto"
                                md="4"
                            >
                                <v-card class="pb-3" border flat>
                                    <v-img :src="img_url">
                                        <div class="d-flex justify-end">
                                            <!-- <v-btn
                                                density="comfortable"
                                                v-tooltip:top="'試合動画'"
                                                icon="mdi-video"
                                            ></v-btn> -->
                                            <!-- <v-btn
                                                density="comfortable"
                                                v-tooltip:top="'試合メモ'"
                                                icon="mdi-note-edit-outline"
                                            ></v-btn> -->
                                        </div>
                                    </v-img>

                                    <v-card-item>
                                        <div
                                            v-if="
                                                item.raw.home_team_id ===
                                                myTeam.id
                                            "
                                        >
                                            <v-card-title>
                                                vs
                                                {{ item.raw.away_team_name }}
                                                (H)
                                            </v-card-title>

                                            <v-card-subtitle>
                                                {{
                                                    item.raw
                                                        .away_team_prefecture
                                                }}
                                                |
                                                {{
                                                    item.raw.away_team_category
                                                }}
                                                |
                                                {{ item.raw.away_team_league }}
                                            </v-card-subtitle>
                                        </div>

                                        <div v-else>
                                            <v-card-title>
                                                vs
                                                {{ item.raw.home_team_name }}
                                                (A)
                                            </v-card-title>

                                            <v-card-subtitle>
                                                {{
                                                    item.raw
                                                        .home_team_prefecture
                                                }}
                                                |
                                                {{
                                                    item.raw.home_team_category
                                                }}
                                                |
                                                {{ item.raw.home_team_league }}
                                            </v-card-subtitle>
                                        </div>

                                        <v-card-subtitle>
                                            <v-icon>mdi-calendar-month</v-icon>
                                            {{ item.raw.year }}年{{
                                                item.raw.month
                                            }}月{{ item.raw.day }}日
                                        </v-card-subtitle>
                                        <v-card-subtitle>
                                            <v-icon>
                                                mdi-clock-time-eight-outline
                                            </v-icon>
                                            {{ item.raw.start_time }}
                                            ~
                                            {{ item.raw.end_time }}
                                        </v-card-subtitle>

                                        <v-card-subtitle>
                                            <v-icon
                                                >mdi-map-marker-outline</v-icon
                                            >
                                            {{ item.raw.location }}
                                        </v-card-subtitle>
                                    </v-card-item>
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
