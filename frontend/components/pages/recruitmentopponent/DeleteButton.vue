<script setup>
import { ref } from 'vue';

const dialog = ref(false);

const props = defineProps(['recruitment']);

const emit = defineEmits(['recruitmentDeleted']);

async function deleteRecruitment() {
    const deletedRecruitment = await $fetch(
        `http://localhost:8000/recruitments/${props.recruitment.id}`,
        {
            method: 'DELETE',
        }
    );
    if (deletedRecruitment) {
        // ダイアログを閉じる
        dialog.value = false;
        // イベントを発火して親コンポーネントにプレイヤー情報を渡す
        emit('recruitmentDeleted', deletedRecruitment);
    }
}
</script>

<template>
    <div class="text-center pa-4">
        <v-btn @click="dialog = true" text="削除" elevation="5"></v-btn>

        <v-dialog v-model="dialog" width="auto">
            <v-card max-width="400" title="この募集投稿を削除しますか？">
                <template v-slot:actions>
                    <v-spacer></v-spacer>
                    <v-btn
                        text="キャンセル"
                        variant="plain"
                        @click="dialog = false"
                    ></v-btn>
                    <v-btn
                        color="primary"
                        text="Ok"
                        variant="tonal"
                        @click="deleteRecruitment"
                    ></v-btn>
                </template>
            </v-card>
        </v-dialog>
    </div>
</template>
