<script setup>
import { nextTick, ref, watch } from 'vue';

const user = await getCurrentUser();
const idToken = await user.getIdToken();

const { data: players } = await useFetch('http://localhost:8000/players', {
    method: 'GET',
    headers: {
        Authorization: `Bearer ${idToken}`,
        'Content-Type': 'application/json',
    },
});

const dialog = ref(false);
const dialogDelete = ref(false);
const headers = ref([
    { title: '背番号', align: 'start', key: 'number' },
    { title: 'ポジション', key: 'position', sortable: false },
    { title: '名前', key: 'namae', sortable: false },
    { title: 'Name', key: 'name', sortable: false },
    { title: 'Actions', key: 'actions', sortable: false },
]);

const positions = ['GK', 'DF', 'MF', 'FW'];

const itemId = ref(-1);
const editedIndex = ref(-1);
const editedItem = ref({
    position: '',
    number: null,
    namae: '',
    name: '',
});
const defaultItem = ref({
    position: '',
    number: null,
    namae: '',
    name: '',
});

async function registerPlayer() {
    const registeredPlayer = await $fetch('http://localhost:8000/players', {
        method: 'POST',
        headers: {
            Authorization: `Bearer ${idToken}`,
            'Content-Type': 'application/json',
        },
        body: editedItem.value,
    });

    players.value.push(registeredPlayer);
}

async function editPlayer(id) {
    const editedPlayer = await $fetch(`http://localhost:8000/players/${id}`, {
        method: 'PUT',
        body: editedItem.value,
    });

    Object.assign(players.value[editedIndex.value], editedPlayer);
}

async function deletePlayer(id) {
    await $fetch(`http://localhost:8000/players/${id}`, {
        method: 'DELETE',
    });

    players.value = players.value.filter((player) => player.id !== id);
}

function editItem(item) {
    itemId.value = item.id;
    editedIndex.value = players.value.indexOf(item);
    editedItem.value = Object.assign({}, item);
    dialog.value = true;
}

function close() {
    dialog.value = false;
    nextTick(() => {
        editedItem.value = Object.assign({}, defaultItem.value);
        itemId.value = -1;
        editedIndex.value = -1;
    });
}

async function save() {
    if (editedIndex.value > -1) {
        await editPlayer(itemId.value);
    } else {
        await registerPlayer();
    }
    close();
}

function deleteItem(item) {
    itemId.value = item.id;
    dialogDelete.value = true;
}

function closeDelete() {
    dialogDelete.value = false;
    nextTick(() => {
        itemId.value = -1;
    });
}

function deleteItemConfirm() {
    deletePlayer(itemId.value);
    closeDelete();
}

watch(dialog, (val) => {
    val || close();
});

watch(dialogDelete, (val) => {
    val || closeDelete();
});

const isValid = computed(() => {
    return (
        editedItem.value.position &&
        editedItem.value.number &&
        editedItem.value.namae &&
        editedItem.value.name
    );
});
</script>

<template>
    <div>
        <v-data-table
            :headers="headers"
            :items="players"
            :sort-by="[{ key: 'number', order: 'asc' }]"
        >
            <template v-slot:top>
                <v-toolbar flat>
                    <v-toolbar-title>選手一覧</v-toolbar-title>
                    <v-divider class="mx-4" inset vertical></v-divider>
                    <v-spacer></v-spacer>
                    <v-dialog v-model="dialog" max-width="500px">
                        <!-- <template v-slot:activator="{ props }">
                            <v-btn
                                prepend-icon="mdi-account-plus"
                                elevation="5"
                                v-bind="props"
                            >
                                選手を登録
                            </v-btn>
                        </template> -->
                        <v-card prepend-icon="mdi-account" title="選手情報">
                            <v-card-text>
                                <v-container>
                                    <v-row>
                                        <v-col cols="12" md="4" sm="6">
                                            <v-select
                                                v-model="editedItem.position"
                                                label="ポジション"
                                                :items="positions"
                                            ></v-select>
                                        </v-col>
                                        <v-col cols="12" md="4" sm="6">
                                            <v-number-input
                                                v-model="editedItem.number"
                                                label="背番号"
                                                :min="1"
                                                control-variant="stacked"
                                            >
                                            </v-number-input>
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col>
                                            <v-responsive
                                                class="mx-auto"
                                                max-width="344"
                                            >
                                                <v-text-field
                                                    v-model="editedItem.namae"
                                                    label="名前"
                                                    clearable
                                                ></v-text-field>
                                            </v-responsive>
                                        </v-col>
                                        <v-responsive
                                            class="mx-auto"
                                            max-width="344"
                                        >
                                            <v-col>
                                                <v-text-field
                                                    v-model="editedItem.name"
                                                    label="Name"
                                                    clearable
                                                ></v-text-field>
                                            </v-col>
                                        </v-responsive>
                                    </v-row>
                                </v-container>
                            </v-card-text>

                            <v-divider></v-divider>

                            <v-card-actions>
                                <v-spacer></v-spacer>

                                <v-btn
                                    text="キャンセル"
                                    variant="plain"
                                    @click="close"
                                >
                                </v-btn>

                                <v-btn
                                    color="primary"
                                    text="保存"
                                    variant="tonal"
                                    @click="save"
                                    :disabled="!isValid"
                                >
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                    <v-dialog v-model="dialogDelete" max-width="500px">
                        <v-card
                            prepend-icon="mdi-alert-circle-outline"
                            title="この選手情報を削除してもよろしいですか？"
                        >
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn
                                    text="キャンセル"
                                    variant="plain"
                                    @click="closeDelete"
                                ></v-btn>
                                <v-btn
                                    color="primary"
                                    text="OK"
                                    variant="tonal"
                                    @click="deleteItemConfirm"
                                ></v-btn>
                                <v-spacer></v-spacer>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </v-toolbar>
            </template>
            <template v-slot:[`item.actions`]="{ item }">
                <v-icon
                    color="#4CAF50"
                    class="me-2"
                    @click="editItem(item)"
                    v-tooltip:top="'編集'"
                >
                    mdi-pencil
                </v-icon>
                <v-icon
                    color="#F44336"
                    class="me-2"
                    @click="deleteItem(item)"
                    v-tooltip:top="'削除'"
                >
                    mdi-delete
                </v-icon>
            </template>
            <template v-slot:no-data> 選手が登録されていません </template>
        </v-data-table>
    </div>
</template>
