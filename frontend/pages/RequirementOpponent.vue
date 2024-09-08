<script setup>
import RecruitmentCard from '~/components/pages/recruitmentopponent/RecruitmentCard.vue';
import PostButton from '~/components/pages/recruitmentopponent/PostButton.vue';

const { data: recruitments } = await useFetch(
    'http://localhost:8000/recruitments'
);

function handleRecruitmentPosted(newRecruitment) {
    recruitments.value.push(newRecruitment);
}

function handlerecruitmentDeleted(deletedrecruitment) {
    recruitments.value = recruitments.value.filter(
        (recruitment) => recruitment.id !== deletedrecruitment.id
    );
}
</script>

<template>
    <div>
        <v-row class="d-flex align-end justify-end"
            ><PostButton @recruitmentPosted="handleRecruitmentPosted"
        /></v-row>
        <div
            v-if="recruitments.length === 0"
            class="d-flex align-center justify-center"
            style="min-height: 300px"
        >
            <v-empty-state
                icon="mdi-text-box-outline"
                title="募集が投稿されていません"
            >
            </v-empty-state>
        </div>
        <div v-else>
            <v-row>
                <v-col
                    v-for="(recruitment, i) in recruitments"
                    :key="i"
                    cols="12"
                    md="4"
                >
                    <RecruitmentCard
                        :recruitment="recruitment"
                        @recruitmentDeleted="handlerecruitmentDeleted"
                    />
                </v-col>
            </v-row>
        </div>
    </div>
</template>
