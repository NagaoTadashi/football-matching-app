<script setup>
const { data: team_info } = await useFetch('http://localhost:8000/team_info');
</script>

<template>
    <div v-if="team_info === null">
        <v-empty-state
            icon="mdi-tshirt-crew"
            title="チーム情報が登録されていません"
        >
        </v-empty-state>
    </div>
</template>
