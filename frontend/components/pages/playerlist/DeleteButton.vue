<script setup>
import { ref } from 'vue';

const dialog = ref(false);

const props = defineProps(['player']);

const emit = defineEmits(['playerDeleted']);

async function deletePlayer() {
    const deletedPlayer = await $fetch(
        `http://localhost:8000/players/${props.player.id}`,
        {
            method: 'DELETE',
        }
    );
    if (deletedPlayer) {
        // ダイアログを閉じる
        dialog.value = false;
        // イベントを発火して親コンポーネントにプレイヤー情報を渡す
        emit('playerDeleted', deletedPlayer);
    }
}
</script>

<template>
    <div class="text-center pa-4">
        <v-btn @click="dialog = true" text="削除" elevation="5"></v-btn>

        <v-dialog v-model="dialog" width="auto">
            <v-card max-width="400" title="この選手を削除しますか？">
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
                        @click="deletePlayer"
                    ></v-btn>
                </template>
            </v-card>
        </v-dialog>
    </div>
</template>
