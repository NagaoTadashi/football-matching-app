<script setup>
import RegisterButton from '~/components/pages/teaminfo/RegisterButton.vue';
import EditButton from '~/components/pages/teaminfo/EditButton.vue';

const { data: teamInfo } = await useFetch('http://localhost:8000/team_info');

function handleTeamInfoRegisterd(newTeamInfo) {
    teamInfo.value = newTeamInfo;
}

function handleTeamInfoEdited(updatedTeamInfo) {
    teamInfo.value = updatedTeamInfo;
}
</script>

<template>
    <div>
        <div v-if="teamInfo === null">
            <v-empty-state
                class="d-flex align-center justify-center"
                style="min-height: 300px"
                icon="mdi-tshirt-crew"
                title="チーム情報が登録されていません"
                ><RegisterButton @TeamInfoRegisterd="handleTeamInfoRegisterd" />
            </v-empty-state>
        </div>
        <div v-else>
            <v-row class="d-flex align-end justify-end">
                <EditButton
                    :teamInfo="teamInfo"
                    @TeamInfoEdited="handleTeamInfoEdited"
                />
            </v-row>

            <v-row justify="center">
                <v-col cols="12" sm="20" md="20">
                    <v-card>
                        <v-row no-gutters>
                            <v-col cols="12" sm="6">
                                <v-card-title class="text-h4">{{
                                    teamInfo.name
                                }}</v-card-title>
                                <br />

                                <v-card-subtitle class="text-h6"
                                    >地域:
                                    {{ teamInfo.region }}</v-card-subtitle
                                >
                                <br />

                                <v-card-subtitle class="text-h6"
                                    >都道府県:
                                    {{ teamInfo.prefecture }}</v-card-subtitle
                                >
                                <br />

                                <v-card-subtitle class="text-h6"
                                    >カテゴリ:
                                    {{ teamInfo.category }}</v-card-subtitle
                                >
                                <br />

                                <v-card-subtitle class="text-h6"
                                    >所属リーグ:
                                    {{ teamInfo.league }}</v-card-subtitle
                                >
                            </v-col>
                            <v-col cols="12" sm="6">
                                <v-img
                                    src="https://cdn.pixabay.com/photo/2015/07/02/00/08/football-828218_1280.jpg"
                                    class="fill-height"
                                ></v-img>
                            </v-col>
                        </v-row>
                    </v-card>
                </v-col>
            </v-row>
        </div>
    </div>
</template>
