import { firestore, storage } from './firebaseConfig';

// Function to create a new document in a specified collection
export const createDocument = async (collection, data) => {
    try {
        const docRef = await firestore.collection(collection).add(data);
        return docRef.id;
    } catch (error) {
        console.error('Error adding document: ', error);
        throw error;
    }
};

// Function to upload file to Firebase Storage
export const uploadFile = async (path, file) => {
    try {
        const storageRef = storage.ref();
        const fileRef = storageRef.child(path);
        await fileRef.put(file);
        return await fileRef.getDownloadURL();
    } catch (error) {
        console.error('Error uploading file: ', error);
        throw error;
    }
};
